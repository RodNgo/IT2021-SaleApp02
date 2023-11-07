def load_categories():
    return [{
        'id': 1,
        'name': 'Mobile'
    }, {
        'id': 2,
        'name': 'Tablet'
    }]


def load_product(kw=None):
    produts = [{
        "id": 1,
        "name": 'IPhone 15 Pro Max 256GB | Chính Hãng VN/A',
        "price": "39.790.000",
        "image": "https://cellphones.com.vn/media/catalog/product/i/p/iphone-15-pro-max_3.png"
    }, {
        "id": 2,
        "name": 'MacBook Air 15 inch M2 2023 16GB 256GB | Chính hãng Apple',
        "price": "36.990.000",
        "image": "https://cellphones.com.vn/media/catalog/product/a/i/air_m2_256gb_1.png"
    }, {
        "id": 3,
        "name": 'Samsung Galaxy Z Flip5 256GB',
        "price": "19.990.000",
        "image": "https://cellphones.com.vn/media/catalog/product/s/a/samsung-galaxy-z-flip-5-256gb_1_4.png"
    }, {
        "id": 4,
        "name": 'Iphone 15 Pro Max',
        "price": 20000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1690461425/bqjr27d0xjx4u78ghp3s.jpg"
    }, {
        "id": 5,
        "name": 'Iphone 15 Pro Max',
        "price": 20000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1690461425/bqjr27d0xjx4u78ghp3s.jpg"
    }, {
        "id": 6,
        "name": 'Iphone 15 Pro Max',
        "price": 20000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1690461425/bqjr27d0xjx4u78ghp3s.jpg"
    }, {
        "id": 7,
        "name": 'Iphone 15 Pro Max',
        "price": 20000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1690461425/bqjr27d0xjx4u78ghp3s.jpg"
    }, {
        "id": 8,
        "name": 'Ipad Pro 2022',
        "price": 20000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1690461425/bqjr27d0xjx4u78ghp3s.jpg"
    }
    ]

    if kw:
        produts = [p for p in produts if p['name'].find(kw) >= 0]

    return produts
