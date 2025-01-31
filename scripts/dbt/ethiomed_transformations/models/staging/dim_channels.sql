{{ config(materialized='table') }}

SELECT
    channel,
    COUNT(*) AS total_messages,
    MIN(message_date) AS first_message_date,
    MAX(message_date) AS last_message_date
FROM {{ ref('stg_raw_messages') }}
GROUP BY 1
