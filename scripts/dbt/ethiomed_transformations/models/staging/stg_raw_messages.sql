{{ config(materialized='view') }}

WITH raw_data AS (
    SELECT
        message_id,
        channel,
        text,
        date,
        media_path,
        ROW_NUMBER() OVER (
            PARTITION BY message_id, channel 
            ORDER BY date DESC
        ) AS row_num
    FROM {{ source('raw', 'raw_messages') }}
)

