import pytest


@pytest.fixture(params=[(4, 5, 20),
                        (4.5, 5.5, 24.75)],
                ids=["integer", "float"])
def get_rectangle_positive(request):
    print("\n Start DB")
    yield request.param
    print("\n Stop DB")


@pytest.fixture(params=[(-4, 5, -20),
                        (-4.5, -5.5, 24.75)],
                ids=["integer", "float"])
def get_rectangle_negative(request):
    print("\n Start DB")
    yield request.param
    print("\n Stop DB")


@pytest.fixture(params=[(4, 5, 3, 6),
                          (4.5, 5.5, 3.5, 7.85)],
                ids=["integer", "float"])
def get_triangle_positive(request):
    print("\n Start DB")
    yield request.param
    print("\n Stop DB")


@pytest.fixture(params=[(-4, 5, 3, 6),
                        (-4.5, 5.5, 3.5, 7.85)],
                ids=["integer", "float"])
def get_triangle_negative(request):
    print("\n Start DB")
    yield request.param
    print("\n Stop DB")


@pytest.fixture(params=[(4, 50.27),
                        (4.5, 63.62)],
                ids=["integer", "float"])
def get_circle_positive(request):
    print("\n Start DB")
    yield request.param
    print("\n Stop DB")


@pytest.fixture(params=[(-4, 50.27),
                        (-4.5, 63.62)],
                ids=["integer", "float"])
def get_circle_negative(request):
    print("\n Start DB")
    yield request.param
    print("\n Stop DB")


@pytest.fixture(params=[(4, 16),
                        (4.5, 20.25)],
                ids=["integer", "float"])
def get_square_positive(request):
    print("\n Start DB")
    yield request.param
    print("\n Stop DB")


@pytest.fixture(params=[(-4, 16),
                        (-4.5, 20.25)],
                ids=["integer", "float"])
def get_square_negative(request):
    print("\n Start DB")
    yield request.param
    print("\n Stop DB")
