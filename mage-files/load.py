from mage_ai.settings.repo import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_big_query(data: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to a BigQuery warehouse.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#bigquery
    """
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'
    
    # key is the table name, value is the actual json data
    for table_name, data in data.items():
        # create table_id which is a string of the bigquery location using the table name
        table_id = 'my-test-project-481010.uber_data_engineering.{}'.format(table_name)
        BigQuery.with_config(ConfigFileLoader(config_path, config_profile)).export(
            DataFrame(data), 
            table_id,
            if_exists='replace',  # Specify resolution policy if table name already exists
        )