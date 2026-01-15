# Uber Data Analytics | Data Engineering GCP Project

## Introduction
The project showcases an end-to-end data engineering and analytics pipeline built using Uber trip data. The goal is to ingest raw trip
records, perform transformations and data modelling, and surface business and operational insights via visualisations. The project leverages a
modern data engineering stack including GCP services and tools, demonstrating core data engineering concepts including ingestion, transformation, modelling, 
and analytics delivery.

## Data Pipeline Architecture 
![Data Pipeline Architecture](https://github.com/gc222/Uber-Data-Analytics/blob/main/architecture.jpg)

1. **Data Ingestion and Storage**
   - The trip records data is stored in Google Cloud Storage serving as the staging area for the raw unprocessed data. 

2. **Data Processing**
   - Mage is used to create and execute the ETL scripts for processing the data. 
   - Google Compute Engine is used to create and manage a virtual machine to host Mage.

3. **Data Warehouse and Analytics**
   - Google BigQuery is a data warehouse platform to store the processed the data and perform queries and analysis. 

4. **Data Visualisation**
   - The final component is Looker Studio for developing an interactive MI / Operations dashboard that delivers insights to business users.

## Technology Stack
**Programming Language**
- **Python** - Used to write the ETL scripts in Mage which defines the data processing logic.

**Google Cloud Platform (GCP) components:**
1. **Cloud Storage (GCS)** - A scalable, efficient, and secure cloud storage serving as the data lake.
2. **Compute Engine (GCE)** - An IaaS that provides the ability to create and run virtual machine instances for various workloads.
3. **BigQuery (GBQ)** - A data warehouse platform for managing and executing queries with the dataset.
4. **Looker Studio** - A business intelligence tool that have direct integration to its own Google products to create visualisations.

**Data Pipeline Tool** 
- **Mage** - An ETL orchestration and transformation tool to create and manage data workflows.



Dataset
The dataset used in this project is sourced from TLC Trip Record Data Yellow and Green taxi records which includes key fields 
capturing vendor, pick-up and drop-off date/times, pick-up and drop-off locations, trip distances, itemized fares, rate types, payment types, 
and driver-reported passenger counts.

More information about the dataset can be found here:
1. Website link: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
2. Data Dictionary: https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf



## Data Model
![Data Model](https://github.com/gc222/Uber-Data-Analytics/blob/main/data_model.jpeg)




1. **Data Ingestion and Storage**
   - The trip records data is stored in Google Cloud Storage serving as the staging area for the raw unprocessed data. 

2. **Data Processing**
   - The Mage data pipeline tool runs the ETL scripts extracting the data from GCS, performing transformations, and load it into 

4. Transformation
