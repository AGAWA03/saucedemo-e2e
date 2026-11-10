from playwright.sync_api import expect

def test_six_products_displayed(logged_in):
    expect(logged_in.items).to_have_count(6)

def test_sort_name_a_to_z(logged_in):
    logged_in.sort_by("Name (A to Z)")
    names = logged_in.item_names.all_inner_texts()
    assert names == sorted(names)

def test_sort_name_z_to_a(logged_in):
    logged_in.sort_by("Name (Z to A)")
    names = logged_in.item_names.all_inner_texts()
    assert names == sorted(names, reverse=True)

def test_sort_price_low_to_high(logged_in):
    logged_in.sort_by("Price (low to high)")
    prices = [float(p.replace("$", "")) for p in logged_in.item_prices.all_inner_texts()]
    assert prices == sorted(prices)

def test_sort_price_high_to_low(logged_in):
    logged_in.sort_by("Price (high to low)")
    prices = [float(p.replace("$", "")) for p in logged_in.item_prices.all_inner_texts()]
    assert prices == sorted(prices, reverse=True)