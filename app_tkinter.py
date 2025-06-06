import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class CalculadoraPropina(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de Propinas")
        self.resizable(False, False)
        self._crear_widgets()

    def _crear_widgets(self):
        
        lbl_monto = ttk.Label(self, text="Monto de la cuenta ($):")
        lbl_monto.grid(row=0, column=0, padx=10, pady=(10, 2), sticky="w")

        self.entry_monto = ttk.Entry(self)
        self.entry_monto.grid(row=0, column=1, padx=10, pady=(10, 2))
        self.entry_monto.focus()

        
        porcentajes = [("10 %", 0.10), ("15 %", 0.15), ("20 %", 0.20)]
        frm_botones = ttk.Frame(self)
        frm_botones.grid(row=1, column=0, columnspan=2, pady=(5, 15))

        for idx, (texto, valor) in enumerate(porcentajes):
            btn = ttk.Button(frm_botones, text=texto, 
                             command=lambda v=valor: self._calcular_propina(v))
            btn.grid(row=0, column=idx, padx=5)

        
        lbl_result_titulo = ttk.Label(self, text="Resultados:")
        lbl_result_titulo.grid(row=2, column=0, padx=10, pady=(0, 2), sticky="w")

        self.lbl_propina = ttk.Label(self, text="Propina: $ 0.00")
        self.lbl_propina.grid(row=3, column=0, padx=10, pady=(0, 2), columnspan=2, sticky="w")

        self.lbl_total = ttk.Label(self, text="Total a pagar: $ 0.00")
        self.lbl_total.grid(row=4, column=0, padx=10, pady=(0, 10), columnspan=2, sticky="w")

    def _calcular_propina(self, porcentaje):
        
        texto_monto = self.entry_monto.get().strip()
        try:
           
            monto = float(texto_monto)
            if monto < 0:
                raise ValueError("El monto no puede ser negativo.")
        except ValueError:
            messagebox.showerror("Error de entrada", "Ingresa un monto válido (número).")
            return

        propina = monto * porcentaje
        total = monto + propina

        
        self.lbl_propina.config(text=f"Propina ({int(porcentaje*100)} %): $ {propina:,.2f}")
        self.lbl_total.config(text=f"Total a pagar: $ {total:,.2f}")

if __name__ == "__main__":
    app = CalculadoraPropina()
    app.mainloop()
