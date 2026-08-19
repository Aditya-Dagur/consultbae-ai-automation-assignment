import pandas as pd

# Load files
df1 = pd.read_csv("../data/source1_naukri_applicants.csv")
df2 = pd.read_csv("../data/source2_gig_workers.csv")
df3 = pd.read_csv("../data/source3_cbnexus_contacts.csv")

# Rename columns
df1 = df1.rename(
    columns={
        "Full Name": "name",
        "Email": "email",
        "Phone": "phone",
        "City": "city",
        "Skills": "skills",
    }
)

df2 = df2.rename(
    columns={
        "worker_name": "name",
        "email_id": "email",
        "location": "city",
        "skill_tags": "skills",
    }
)

df3 = df3.rename(
    columns={
        "Name": "name",
        "Phone Number": "phone",
        "City": "city",
    }
)

# Add missing columns
for df in [df1, df2, df3]:
    for column in ["name", "email", "phone", "city", "skills"]:
        if column not in df.columns:
            df[column] = None

# Keep only common columns
columns = ["name", "email", "phone", "city", "skills"]

df1 = df1[columns]
df2 = df2[columns]
df3 = df3[columns]

# Merge
merged = pd.concat([df1, df2, df3])

# Remove duplicates
merged = merged.drop_duplicates(
    subset=["email", "phone"],
    keep="first"
)

# Save
merged.to_csv("../database/merged.csv", index=False)

print("Records after merge:", len(merged))
print("Saved to database/merged.csv")