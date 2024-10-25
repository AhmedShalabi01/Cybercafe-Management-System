import pandas as pd


class drinks:
    def __init__(self, drink_name=None, drink_Price=None):
        self.__drink_name = drink_name
        self.__drink_Price = drink_Price
        self.__Drink_id = None
        if self.__drink_name != None and self.__drink_Price != None:
            try:
                df1 = pd.read_csv("databases/Drinks_menu_Tbl.CSV", index_col=[0])

                df2 = pd.DataFrame(
                    {
                        "drink_name": self.__drink_name,
                        "drink_price": self.__drink_Price,
                    },
                    index=[1],
                )

                df = pd.concat([df1, df2], ignore_index=True)
                df.to_csv("databases/Drinks_menu_Tbl.CSV")
                print("Drink was Added successfully!")
            except FileNotFoundError:
                print("CSV file not found")
            except:
                print("something went very wrong")

    # def add_drink(self,drink_name,drink_Price):
    #     try:
    #         self.__drink_name = drink_name
    #         self.__drink_Price = drink_Price

    #         df1 = pd.read_csv('databases/Drinks_menu_Tbl.CSV', index_col=[0])

    #         df2 = pd.DataFrame({"drink_name":self.__drink_name,
    #                                 'drink_price':self.__drink_Price,}
    #                                 ,index=[1])

    #         df = pd.concat([df1,df2],ignore_index=True)
    #         df.to_csv('databases/Drinks_menu_Tbl.CSV')
    #         print('Drink was Added successfully!')
    #     except FileNotFoundError:
    #         print('CSV file not found')
    #     except:
    #         print('something went very wrong')

    def Show_All_Drinks(self):
        try:
            return pd.read_csv("databases/Drinks_menu_Tbl.CSV", index_col=[0])
        except FileNotFoundError:
            return "CSV file not found"
        except:
            return "something went very wrong"

    def Update_Record(self, Drink_id, drink_name, drink_Price):
        try:
            df = pd.read_csv("databases/Drinks_menu_Tbl.CSV", index_col=[0])

            self.__drink_name = drink_name
            self.__drink_Price = drink_Price
            self.__Drink_id = Drink_id

            # df.at[Drink_id,["drink_name","drink_price"]] =['yyy',5555]
            df.loc[self.__Drink_id] = [self.__drink_name, self.__drink_Price]
            df.to_csv("databases/Drinks_menu_Tbl.CSV")
            print("Drink was updated successfully!")
        except KeyError:
            print("Invalid drink ID")
        except FileNotFoundError:
            print("CSV file not found")
        except:
            print("something went very wrong")

    def Delete_Drink_by_index(self, Drink_id):
        try:
            self.__Drink_id = Drink_id
            df = pd.read_csv("databases/Drinks_menu_Tbl.CSV", index_col=[0])
            df = df.drop(self.__Drink_id)
            df.to_csv("databases/Drinks_menu_Tbl.CSV")
            print("Drink was deleted successfully!")
        except KeyError:
            print("Invalid computer ID")
        except FileNotFoundError:
            print("CSV file not found")
        except:
            print("something went very wrong")

    def Search_Record(self, Key_word):
        try:
            df = pd.read_csv("databases/Drinks_menu_Tbl.CSV", index_col=[0])
            return df[
                df.apply(
                    lambda row: row.astype(str).str.contains(Key_word).any(), axis=1
                )
            ]
        except FileNotFoundError:
            return "CSV file not found"
        except:
            return "something went very wrong"

    def Buy_a_drink(self, Session_id, Drink_id):
        try:

            drink_df = pd.read_csv("databases/Drinks_menu_Tbl.CSV", index_col=[0])

            if Drink_id not in drink_df.index.values:
                print("invalid Drink id")
            else:

                df1 = pd.read_csv("databases/Sold_drinks_Tbl.CSV", index_col=[0])

                df2 = pd.DataFrame(
                    {
                        "Drink_id": Drink_id,
                        "Session_id": Session_id,
                    },
                    index=[1],
                )

                df = pd.concat([df1, df2], ignore_index=True)
                df.to_csv("databases/Sold_drinks_Tbl.CSV")
                print("Drink was Added successfully!")
        except FileNotFoundError:
            print("CSV file not found")
        except:
            print("something went very wrong")

    def Calculate_Drinks_Cost(self, Session_id):
        try:
            Sold_drinks_Tbl = pd.read_csv(
                "databases/Sold_drinks_Tbl.CSV", index_col=[0]
            )
            Drinks_menu_Tbl = pd.read_csv(
                "databases/Drinks_menu_Tbl.CSV", index_col=[0]
            )

            df = pd.merge(
                Sold_drinks_Tbl,
                Drinks_menu_Tbl["drink_price"],
                how="inner",
                left_on="Drink_id",
                right_index=True,
            )

            if Sold_drinks_Tbl.empty:
                return 0
            if Session_id not in df["Session_id"].values:
                return 0
            return df[df["Session_id"] == Session_id]["drink_price"].sum()

        except FileNotFoundError:
            return "CSV file not found"
        except:
            return "something went very wrong"
