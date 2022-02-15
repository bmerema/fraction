def on_barcode(barcode):
    global amount
    if barcode != "":
        amount = "$11.50"
    else:
        try:
            int(barcode)
            amount = "$11.50"
        except:
            amount = "invalid"

def last_text_displayed():
    return amount


def test_output_test():
    assert on_barcode('12345')=="7,95"



