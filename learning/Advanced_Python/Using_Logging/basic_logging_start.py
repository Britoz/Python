# demonstrate using of logging
'''
logging usually used debugging
'''
import logging

# TODO: use the build-in logging module

def main():
    # TODO: use basicConfig to configure logging
    logging.basicConfig(level=logging.DEBUG, filename="output.log", filemode="w")
    '''
    set the basic config
    allow debug and critical to display on Run
    
    the basicConfig is only executed once before logging starts.
    once logging is started, then subsequent calls to this function
    won't have any effect
    
    filename: create a file which is used to store all debugging
    '''

    # Try out each of the log levels
    logging.debug("This is a debug message")
    logging.info("This is a info message")
    logging.warning("This is a warning message")
    logging.error("This is a error message")
    logging.critical("This is a critical message")
    '''
    there are 5 different of logging functions

    logging.debug("debug-level message")
    -- Diagnostic information useful for debugging

    logging.info("info-level message")
    -- General information about program execution results

    logging.warning("warning-level message")
    -- Something unexpected, or an approaching problem

    logging.error("error-level message")
    -- Unable to perform a specific operation due to problem

    logging.critical("critical-level message")
    -- program may not be able to continue, serious error
    '''

    # TODO: Output formatted strings to the log
    logging.info("Here's a {} variable and an int:".format("string", 10))

if __name__ == '__main__':
    main()