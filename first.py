# Import the Session class from the snowflake.snowpark.session module
from snowflake.snowpark.session import Session

# Create Session object
def create_session_object():
    # Define the connection parameters
    connection_parameters = {
account = "QECGRSE-HJC54946"
user = "SIRANYAM"
password = "Nare2819#npdv1"
role = "SYSADMIN"
warehouse = "COMPUTE_WH"
database = "SMOOTHIES"
schema = "PUBLIC"
client_session_keep_alive = true 


"account": "__INSERT_ACCOUNT_HERE__",
      "user": "__INSERT_USERNAME_HERE__",
      "password": "__INSERT_PASSWORD_HERE__",
      "role": "__INSERT_ROLE_HERE__",
      "warehouse": "__INSERT_WAREHOUSE_HERE__",
      "database": "__INSERT_DATABASE_HERE__",
      "schema": "__INSERT_SCHEMA_HERE__"
    }
    
    
    # Create the session object with the provided connection parameters
    session = Session.builder.configs(connection_parameters).create()
    
    # Print the contents of your session object
    # Print(session)
    
    return session 
    
    
# Function call    
create_session_object()
