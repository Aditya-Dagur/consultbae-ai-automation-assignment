import pandas as pd

files = [
    "../data/source1_naukri_applicants.csv",
    "../data/source2_gig_workers.csv",
    "../data/source3_cbnexus_contacts.csv"
]

for file in files:
    df = pd.read_csv(file)

    print("\n" + "=" * 50)
    print(file)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nShape:")
    print(df.shape)

    print("\nMissing values:")
    print(df.isnull().sum())