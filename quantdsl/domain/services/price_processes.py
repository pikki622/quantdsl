from quantdsl.exceptions import DslError
from quantdsl.priceprocess.base import PriceProcess


def get_price_process(price_process_name):
    # Load the price process object.
    assert price_process_name, "Price process name is required"
    price_process_module_name, price_process_class_name = price_process_name.rsplit('.', 1)
    try:
        price_process_module = __import__(price_process_module_name, '', '', '*')
    except Exception as e:
        raise DslError(
            f"Can't import price process module '{price_process_module_name}': {e}"
        )
    try:
        price_process_class = getattr(price_process_module, price_process_class_name)
    except Exception as e:
        raise DslError(
            f"Can't find price process class '{price_process_class_name}' in module '{price_process_module_name}': {e}"
        )
    assert issubclass(price_process_class, PriceProcess)
    return price_process_class()
