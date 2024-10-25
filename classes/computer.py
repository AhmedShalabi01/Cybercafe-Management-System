import pandas as pd


class computer:
    def __init__(self, cpu=None, ram=None, gpu=None, storage=None):
        self.__cpu = cpu
        self.__ram = ram
        self.__gpu = gpu
        self.__storage = storage
        self.__computer_id = None
        self.__available = 0
        if (
            self.__cpu != None
            and self.__ram != None
            and self.__gpu != None
            and self.__storage != None
        ):
            try:
                df1 = pd.read_csv("databases/Computer_Tbl.CSV", index_col=[0])

                df2 = pd.DataFrame(
                    {
                        "cpu": self.__cpu,
                        "ram": self.__ram,
                        "gpu": self.__gpu,
                        "storage": self.__storage,
                        "available": self.__available,
                    },
                    index=[1],
                )

                df = pd.concat([df1, df2], ignore_index=True)
                df.to_csv("databases/Computer_Tbl.CSV")
                print("Computer was Added successfully!")
            except FileNotFoundError:
                print("CSV file not found")
            except:
                print("something went very wrong")

    # def Add_New_Computer(self,cpu,ram,gpu,storage):
    #     try:
    #         self.__cpu = cpu
    #         self.__ram = ram
    #         self.__gpu = gpu
    #         self.__storage = storage
    #         self.__available = 0

    #         df1 = pd.read_csv('databases/Computer_Tbl.CSV', index_col=[0])

    #         df2 = pd.DataFrame({"cpu":self.__cpu,
    #                                 'ram':self.__ram,
    #                                 'gpu':self.__gpu,
    #                                 'storage':self.__storage,
    #                                 'available':self.__available}
    #                                 ,index=[1])

    #         df = pd.concat([df1,df2],ignore_index=True)
    #         df.to_csv('databases/Computer_Tbl.CSV')
    #         print('Computer was Added successfully!')
    #     except FileNotFoundError:
    #         print('CSV file not found')
    #     except:
    #         print('something went very wrong')

    def Show_All_Computers(self):
        try:
            return pd.read_csv("databases/Computer_Tbl.CSV", index_col=[0])
        except FileNotFoundError:
            return "CSV file not found"
        except:
            return "something went very wrong"

    def Update_Record(self, computer_id, cpu, ram, gpu, storage):
        try:
            df = pd.read_csv("databases/Computer_Tbl.CSV", index_col=[0])

            self.__cpu = cpu
            self.__ram = ram
            self.__gpu = gpu
            self.__storage = storage
            self.__computer_id = computer_id
            self.__available = 0

            df.at[self.__computer_id, "cpu"] = self.__cpu
            df.at[self.__computer_id, "ram"] = self.__ram
            df.at[self.__computer_id, "gpu"] = self.__gpu
            df.at[self.__computer_id, "storage"] = self.__storage
            df.at[self.__computer_id, "available"] = self.__available

            # df.loc[self.__computer_id] = [self.__ram,self.__gpu,self.__storage,self.__cpu]
            df.to_csv("databases/Computer_Tbl.CSV")
            print("Computer was updated successfully!")

        except KeyError:
            print("Invalid computer ID")
        except FileNotFoundError:
            print("CSV file not found")
        except:
            print("something went very wrong")

    def Delete_Computer_by_index(self, x):
        try:
            df = pd.read_csv("databases/Computer_Tbl.CSV", index_col=[0])
            df = df.drop(x)
            df.to_csv("databases/Computer_Tbl.CSV")
            print("Computer was deleted successfully!")
        except KeyError:
            print("Invalid computer ID")
        except FileNotFoundError:
            print("CSV file not found")
        except:
            print("something went very wrong")

    def Search_Record(self, Key_word):
        try:
            df = pd.read_csv("databases/Computer_Tbl.CSV", index_col=[0])
            dfs = df[
                df.apply(
                    lambda row: row.astype(str).str.contains(Key_word).any(), axis=1
                )
            ]
            if dfs.empty:
                return "Not Found"
            return df[
                df.apply(
                    lambda row: row.astype(str).str.contains(Key_word).any(), axis=1
                )
            ]

        except FileNotFoundError:
            return "CSV file not found"
        except:
            return "something went very wrong"
