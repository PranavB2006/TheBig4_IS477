"""Clean CDC PLACES and USDA county data for the IS 477 project."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent
RAW = ROOT / 'data' / 'raw'
PROCESSED = ROOT / 'data' / 'processed'


def fips(series):
    """Convert county identifiers to five-character strings."""
    return series.astype('string').str.strip().str.replace(r'\.0$', '', regex=True).str.zfill(5)


def numeric(series):
    return pd.to_numeric(series.astype('string').str.replace(',', '', regex=False), errors='coerce')


def clean_economic():
    df = pd.read_csv(RAW / 'USDA_Unemployment_and_Median_Household_Income.csv', encoding='latin1', dtype='string')
    df['FIPS'] = fips(df['FIPS_Code'])
    attributes = {'Unemployment_rate_2023': 'unemployment_rate_2023',
                  'Median_Household_Income_2022': 'median_household_income_2022'}
    df = df[df['Attribute'].isin(attributes)].copy()
    df = df[df['FIPS'].str.match(r'^\d{5}$', na=False) & ~df['FIPS'].str.endswith('000')]
    df['Value'] = numeric(df['Value'])
    if df.duplicated(['FIPS', 'Attribute']).any():
        raise ValueError('Duplicate county/attribute rows in economic data')
    out = df.pivot(index='FIPS', columns='Attribute', values='Value').rename(columns=attributes).reset_index()
    return out


def clean_rucc():
    df = pd.read_csv(RAW / 'USDA_Rural_Urban_Continuum_Codes.csv', encoding='latin1', dtype='string')
    df = df[df['Attribute'].eq('RUCC_2023')].copy()
    df['FIPS'] = fips(df['FIPS'])
    df['rucc_2023'] = numeric(df['Value'])
    if df['FIPS'].duplicated().any():
        raise ValueError('Duplicate RUCC county identifiers')
    df['rurality'] = df['rucc_2023'].map(lambda x: 'Metropolitan' if pd.notna(x) and 1 <= x <= 3 else ('Nonmetropolitan' if pd.notna(x) and 4 <= x <= 9 else pd.NA))
    return df[['FIPS', 'State', 'County_Name', 'rucc_2023', 'rurality']].rename(columns={'State': 'state', 'County_Name': 'county'})


def clean_health():
    df = pd.read_csv(RAW / 'CDC_County_Diabetes_and_Obesity_Levels.csv', encoding='latin1', dtype='string')
    df = df[(df['Year'] == '2022') & (df['MeasureId'].isin(['DIABETES', 'OBESITY'])) & (df['Data_Value_Type'] == 'Crude prevalence')].copy()
    df['FIPS'] = fips(df['LocationID'])
    df['Data_Value'] = numeric(df['Data_Value'])
    if df.duplicated(['FIPS', 'MeasureId']).any():
        raise ValueError('Duplicate CDC county/measure rows')
    out = df.pivot(index='FIPS', columns='MeasureId', values='Data_Value').rename(columns={'DIABETES': 'diabetes_pct_2022', 'OBESITY': 'obesity_pct_2022'}).reset_index()
    return out


def main():
    PROCESSED.mkdir(parents=True, exist_ok=True)
    economic, rucc, health = clean_economic(), clean_rucc(), clean_health()
    # RUCC is the county reference list. Left joins retain unmatched counties.
    result = rucc.merge(economic, on='FIPS', how='left', validate='one_to_one')
    result = result.merge(health, on='FIPS', how='left', validate='one_to_one')
    columns = ['FIPS', 'state', 'county', 'rucc_2023', 'rurality',
               'unemployment_rate_2023', 'median_household_income_2022',
               'diabetes_pct_2022', 'obesity_pct_2022']
    result = result[columns].sort_values('FIPS').reset_index(drop=True)
    result.to_csv(PROCESSED / 'cleaned_county_data.csv', index=False)
    fields = columns[3:]
    summary = pd.DataFrame({'field': fields, 'missing_count': [int(result[x].isna().sum()) for x in fields],
                            'nonmissing_count': [int(result[x].notna().sum()) for x in fields]})
    summary['total_counties'] = len(result)
    summary['missing_percent'] = (100 * summary['missing_count'] / len(result)).round(2)
    summary.to_csv(PROCESSED / 'data_quality_summary.csv', index=False)
    required = ['unemployment_rate_2023', 'median_household_income_2022', 'diabetes_pct_2022', 'obesity_pct_2022', 'rucc_2023']
    complete = result[required].notna().all(axis=1).sum()
    print(f'Counties: {len(result):,}; complete counties: {complete:,} ({complete / len(result):.1%})')
    print(summary.to_string(index=False))


if __name__ == '__main__':
    main()
