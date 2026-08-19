# Data Quality Report

| Issue | File | Solution |
| --- | --- | --- |
| Different column names | All files | Standardized column names before merging |
| Missing values | source2_gig_workers.csv | Filled with null values and cleaned before merging |
| Different schemas | All files | Created a unified schema |
| No common unique ID | All files | Used email and phone numbers for record matching |