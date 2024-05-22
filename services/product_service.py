"""
Database Connection 
"""
import psycopg

class ProductService():
    """
    Class Product Service
    with Psycopg
    """
    conn = None

    def __init__(self):

        try:
            self.conn = psycopg.connect("dbname=store user=counter password=counter \
                                        host=localhost port=5432")
        except psycopg.OperationalError as err:
            print(err)
            self.conn.close()

    def read_all(self):
        """ read all registers """
        with self.conn.cursor() as cur:
            data = cur.execute("""
                        SELECT * FROM "product"
                        """)
            return data.fetchall()

    def read_one(self, product_id: str):
        """ Read one product """
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM "product"
                WHERE id = %s
                """, (product_id,))
            data = cur.fetchone()
        return data


    def create(self, data):
        """ create product """
        with self.conn.cursor() as cur:
            print("explotion1")
            cur.execute("""
                        INSERT INTO "product"(name, description, price) 
                        VALUES (%(name)s, %(description)s, %(price)s)
                        """, data)
            print("explotion2", data)
            self.conn.commit()

    def update(self, data):
        """ delete product """
        with self.conn.cursor() as cur:
            cur.execute("""
                        UPDATE  "product" SET name = %(name)s, 
                        description = %(description)s,
                        price = %(price)s WHERE id = %(id)s
                        """, data)
            self.conn.commit()

    def delete(self, product_id: str):
        """ delete product """
        with self.conn.cursor() as cur:
            cur.execute("""
                        DELETE FROM "product" WHERE id = %s
                        """, (product_id,))
            self.conn.commit()

    def __def__(self):
        print("explotion")
        self.conn.close()
