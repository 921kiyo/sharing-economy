
from GLOBALS import DATABASE_URL, PRODUCT_LISTINGS, CHARITY_INFO

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Product, User, Charity

engine = create_engine(DATABASE_URL)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_users():
    for person in PRODUCT_LISTINGS:
        print("Adding", person)
        user = User(name=person)
        session.add(user)

    session.commit()


def add_products():
    for person in PRODUCT_LISTINGS:
        for product in PRODUCT_LISTINGS[person]:
            print("Adding", product["name"], "for", person)

            user = session.query(User).filter_by(name=person).first()
            p = Product(name=product["name"],
                        user_id=user.id,
                        description=product["description"],
                        image=product["url"],
                        price=product["price"],
                        size=product["size"],
                        condition=product["condition"],
                        shipping=product["shipping_cost"]
                        )

            session.add(p)

    session.commit()


def add_charities():
    for charity in CHARITY_INFO:

        c = Charity(name=charity["name"],
                    mission=charity["mission"])

        if charity.get("url") is not None and charity.get("url") != "":
            c.url = charity["url"]

        session.add(c)

    session.commit()


if __name__ == "__main__":

    print("Adding users")
    add_users()

    print("Adding products")
    add_products()





