## Data Storage

### Folder structure
- `data/raw/`: stores raw data files (in csv)
- `data/processed/`: stores processed data files (in parquet)

### We store data in the following formats because
- **csv** is human-readable and the write performance is faster (row-based)
- **parquet** is a more efficient way to handle complex data (column-based)

### Environment variables

The notebook uses environment variables loaded via `dotenv` to define file system paths (`DATA\_DIR\_RAW`, `DATA\_DIR\_PROCESSED`). This ensures data is always read from and written to the correct directories.
