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
   - The final component is Looker Studio for developing an interactive MI / Operations dashboard that delivers business-value insights to stakeholders.

## Technology Stack
**Programming Language**
- **Python** - Used to write the ETL scripts in Mage which defines the data processing logic.

**Google Cloud Platform (GCP) components:**
1. **Cloud Storage (GCS)** - A scalable, efficient, and secure cloud storage serving as the data lake.
2. **Compute Engine (GCE)** - An IaaS that provides the ability to create and run virtual machine instances for various workloads.
3. **BigQuery (GBQ)** - A data warehouse platform for managing and executing queries with the dataset.
4. **Looker Studio** - A business intelligence tool that has direct integration to its own Google products to create visualisations and dashboards.

**Data Pipeline Tool** 
- **Mage** - An ETL orchestration and transformation tool to create and manage data workflows.


## Dataset
The dataset used in this project is sourced from TLC Trip Record Data Yellow and Green taxi records which includes key fields capturing 
- **Pick-up and drop-off dates/times - The data and time of the pick-up and drop-off.
- **Pick-up and drop-off locations - The latitude and longitude coordinates of the pick-up and drop-off locations.
- **Trip distances** - The total elapsed distance of the trip.
- **Itemized fares** - A breakdown of the fares which includes base fare, tax, tips, etc.
- **Rate types** - The final rate code in effect at the end of the trip.
- **Payment types** - The payment method used for the transaction of the trip.
- **Driver-reported passenger counts** - The number of passengers on the trip.

More information about the dataset can be found here:
1. Website link: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
2. Data Dictionary: https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf


## Data Model
![Data Model](https://github.com/gc222/Uber-Data-Analytics/blob/main/data_model.jpeg)

The data model for this project follows the star schema model utilising dimension and fact tables concepts. This is well-suited as it is designed for analytic workloads and optimised for faster querying performance in BigQuery. 

**Dimension tables**
- The qualitative data attributes e.g., pick-up / drop-off locations, payment method, rate codes, etc. are clearly separated into its own table that provides context to the fact tables.

**Fact tables**
- The fact table captures the key business metrics and also contains the foreign keys from the dimension table for clear relationships definitions

**Data Ingestion and Storage**
![Google Cloud Storage](<img width="1574" height="619" alt="image" src="https://github.com/user-attachments/assets/f2448f30-d1fe-4be8-96ad-8f0bc57e5b38" />)


The data is first stored in Google Cloud Storage


**Data Processing in Mage**
In Mage, the workflow is written into individual blocks which separates the ETL logic clearly. 
1. The first stage is to **extract** the data from GCS by providing the url which returns 


1. **Data Ingestion and Storage**
   - The trip records data is stored in Google Cloud Storage serving as the staging area for the raw unprocessed data. 

2. **Data Processing**
   - The Mage data pipeline tool runs the ETL scripts extracting the data from GCS, performing transformations, and load it into 

4. Transformation


