"""
MCP tools for Metabase integration.
"""
import logging

logger = logging.getLogger(__name__)

# Import all tool modules to register their tools
try:
    from . import common
    logger.info("Loaded common tools module")
    
    # Import resources module to ensure it's available for PyInstaller
    from .. import resources
    logger.info("Loaded resources module")
    
    from . import dashboard
    logger.info("Loaded dashboard tools module")
    
    from . import card
    logger.info("Loaded card tools module")
    
    from . import collection
    logger.info("Loaded collection tools module")
    
    from . import database
    logger.info("Loaded database tools module")
    
    from . import search
    logger.info("Loaded search tools module")
    
    from . import dataset
    logger.info("Loaded dataset tools module")
    
    from . import visualization
    logger.info("Loaded visualization tools module")
    
    from . import dashcards
    logger.info("Loaded dashcards tools module")
    
    from . import parameters
    logger.info("Loaded parameters tools module")
    
    from . import enhanced_parameters
    logger.info("Loaded enhanced_parameters tools module")
    
    # Load context tools if enabled
    from ..config import MetabaseConfig
    config = MetabaseConfig.from_env()
    if config.context_auto_inject:
        from . import context
        logger.info("Loaded context tools module")
    else:
        logger.info("Context tools module not loaded (disabled)")
except Exception as e:
    logger.error(f"Error loading tool modules: {e}")
