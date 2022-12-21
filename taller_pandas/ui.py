import tkinter as tk
from pandastable import Table, TableModel
import pandas as pd
from script_dataframe import read_excel, graph_max_values, graph_min_values, graph_count, graph_mode, graph_prom


class DataFrameTable(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__()
        self.parent = parent
        self.pack(fill=tk.BOTH, expand=True)
        # self.button.pack(side=tk.LEFT)
        self.table = Table(
            self, dataframe=df,
            showtoolbar=False,
            showstatusbar=True,
            editable=False)
        self.table.show()


class UI(tk.Tk):
    def __init__(self, df):
        super().__init__()
        self.df = df
        btn_graph_minimum = tk.Button(self, text="Graficar minimo",
                                      fg="black", command=self.graph_minimum)
        btn_graph_minimum.pack()
        btn_graph_maximum = tk.Button(self, text="Graficar maximo",
                                      fg="black", command=self.graph_maximum)
        btn_graph_maximum.pack()
        btn_graph_hist = tk.Button(self, text="Graficar consolidado",
                                   fg="black", command=self.graph_count)
        btn_graph_hist.pack()
        table = DataFrameTable(self, df)

    def graph_maximum(self):
        graph_max_values(self.df)

    def graph_count(self):
        graph_count(self.df)

    def graph_minimum(self):
        graph_min_values(self.df)

    def graph_mode(self):
        graph_mode(self.df)


df = read_excel()
view = UI(df)
view.mainloop()
# table = DataFrameTable(root, df)
# root.mainloop()
