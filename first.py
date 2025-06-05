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
    }
    
    # Create the session object with the provided connection parameters
    session = Session.builder.configs(connection_parameters).create()
    
    # Print the contents of your session object
    # Print(session)
    
    return session 
    
    
# Function call    
create_session_object()
