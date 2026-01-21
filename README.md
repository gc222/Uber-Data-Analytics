# Uber Data Analytics | Data Engineering GCP Project

## Introduction
This project showcases an end-to-end data engineering and analytics pipeline built using Uber trip data. The goal is to ingest raw trip records, perform transformations and data modelling, and surface business and operational insights via interactive visualisations. The project focuses on applying core data engineering principles across the data lifecycle, including cloud-based ingestion, data processing, dimensional modelling, and analytics delivery, using a modern stack of Google Cloud Platform (GCP) services and tools.

## Data Pipeline Architecture 
![Data Pipeline Architecture](https://github.com/gc222/Uber-Data-Analytics/blob/main/architecture.jpg)

1. **Data Ingestion and Storage**
   - Raw trip record data is ingested and stored into Google Cloud Storage which serves as the staging area for unprocessed data. 

2. **Data Processing**
   - Mage is used as the data orchestration and processing tool to implement and execute the ETL workflows. 
   - The Mage environment is hosted on Google Compute Engine (GCE), providing scalable and high-performance virtual machines to run the pipelines without requiring on-premise infrastructure.

3. **Data Warehouse and Analytics**
   - Google BigQuery is a data warehouse platform to store the processed data. BigQuery enables fast, scalable SQL-based querying and supports analytical workloads across large datasets.

4. **Data Visualisation**
   - The final component is Looker Studio to build an interactive Management Information (MI) / Operational dashboard, enabling up-to-date reporting and the delivery of actionable business insights to stakeholders.


## Technology Stack
**Programming Language**
- **Python** - Used to write the ETL scripts in Mage which defines the data processing logic.

**Google Cloud Platform (GCP) components:**
1. **Cloud Storage (GCS)** - A scalable, efficient, and secure cloud storage serving as the data lake.
2. **Compute Engine (GCE)** - An IaaS that provides the ability to create and run virtual machine instances for various workloads using custom configurations.
3. **BigQuery (BQ)** - A data warehouse platform for managing and executing queries with the dataset.
4. **Looker Studio** - A business intelligence tool with native integration to Google products for creating visualisations and dashboards.

**Data Pipeline Tool** 
- **Mage** - An ETL orchestration and transformation tool to create and manage data workflows.


## Dataset
The dataset used in this project is sourced from TLC Trip Record Data Yellow and Green taxi records which include key fields capturing 
- **Pick-up and drop-off dates/times** - The date and time of the pick-up and drop-off.
- **Pick-up and drop-off locations** - The latitude and longitude coordinates of the pick-up and drop-off locations.
- **Trip distances** - The total elapsed distance of the trip.
- **Itemized fares** - A breakdown of the fares which include base fare, tax, tips, etc.
- **Rate types** - The final rate code in effect at the end of the trip.
- **Payment types** - The payment method used for the transaction of the trip.
- **Driver-reported passenger counts** - The number of passengers on the trip.

More information about the dataset can be found here:
1. Website link: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
2. Data Dictionary: https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf


## Data Model
![Data Model](https://github.com/gc222/Uber-Data-Analytics/blob/main/data_model.jpeg)

The data model for this project follows a star schema, utilising fact and dimension tables. This design is well-suited for analytic workloads as it simplifies querying and is optimised for faster querying performance in BigQuery. 

**Dimension tables**
- Qualitative and descriptive attributes (e.g., payment method, rate codes, etc.) are stored in separate dimension tables. These provide contextual information for analysis whilst reducing data redundancy and improving maintainability.

**Fact tables**
- The fact table captures the key business metrics (e.g., fares, tax, etc.) and contains the foreign keys that reference the dimension table, enabling clear relationships and efficient joins for analytical queries.

## 1. Data Ingestion and Storage
<img width="1573" height="618" alt="GCS 2026-01-15 122752" src="https://github.com/user-attachments/assets/cbac011b-61ad-4b43-9cb8-76090e4f1cff" />


The raw unprocessed data is first ingested and stored into Google Cloud Storage acting as the central repository for the pipeline. This is done by creating a globally accessible public bucket, allowing it to be retrieved via API from our ETL scripts. This setup provides scalable and flexible storage for large volumes of data and preserves the raw dataset for reprocessing and downstream transformations.


## 2. Data Processing in Mage
<img width="2131" height="1046" alt="Mage" src="https://github.com/user-attachments/assets/1af220e0-895e-4ac1-b29f-94e6c40a1661" />

In Mage, the end-to-end workflow is implemented into individual blocks which separates the processing logic sequentially. Each block encapsulates a specific stage of the process, making the pipeline easier to understand, maintain, and extend.
1. The first block **loads** the raw data from the GCS bucket using the API URL. Pandas is utilised as a powerful data science library to package it into a dataframe for easier data manipulation and inspection.
2. The second block cleans and **transforms** the data and structures it align with the star schema data model, preparing it for analysis and optimised for faster querying performance.
3. The final block **ingests** the processed data into BigQuery, where tables are created and populated. 

## Visualisation
<img width="1502" height="1128" alt="Uber Dashboard Revenue Overview" src="https://github.com/user-attachments/assets/1c7ae767-47f4-455c-9c50-3bd9312cc943" />

<img width="1502" height="1126" alt="Uber Dashboard Trip Analysis" src="https://github.com/user-attachments/assets/097ace38-d12f-4bdb-9dcb-107abdf04454" />


The processed data is loaded into Looker Studio by creating a live connection with Google's BigQuery. The goal is to create an interactive Management Information (MI) / Operational dashboard, designed to surface KPIs and business critical insights for decision-making. The dashboard is organised into two focused pages with controls to filter on the data:

**Revenue Overview**\
This page provides a high-level view of revenue performance and key financial metrics.
- KPIs: Total Revenue, Avg. Fare Amount, Revenue per Mile
- Revenue Breakdown by Hour of Day (Column Chart)
- Revenue by Vendor ID (Column Chart)
- Revenue by Payment Method (Pie/Donut Chart)
- Total Revenue by Rate Code (Bar Chart)
- Avg. Fare Amount by Rate Code (Bar Chart)
- Trip-level detail table for granular analysis

**Trip Analysis**\
This page focuses on operational performances and trip-level behaviour.
- KPIs: Total Trips, Avg. Trip Distance (mi), Avg. Duration, Total Passengers
- Total Trips Completed over Time (Line Chart)
- Avg. Trip Duration by Rate Code (Bar Chart)
- Trips by Vendor ID (Column Chart)
- No. of Trips by Rate Code (Bar Chart)
- Passenger Count Breakdown (Bar Chart)
- Pickup Location by Rate Code (Bubble Map)

## Conclusion
This project demonstrated the design and implementation of an end-to-end data analytics pipeline using modern data tools. Raw data is ingested and stored in Google Cloud Storage, processed and orchestrated using Mage, and loaded into BigQuery for scalable analytical quering. The final insights are delivered through an interactive Looker Studio dashboard connected directly to the data warehouse.

The architecture follows data engineering best practices, including separation of storage and compute, preservation of raw data for reprocessing, and optimisation of the warehouse for analytical workloads. By structuring the data into fact and dimension tables, the solution enables efficient querying, clear business logic, and flexible reporting.



