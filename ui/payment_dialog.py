from PySide6.QtWidgets import QDialog, QVBoxLayout, QComboBox, QLineEdit, QPushButton, QLabel, QMessageBox
from services.order_service import finalize_order
from services.payment_service import record_payment

class PaymentDialog(QDialog):
    def __init__(self, cart, cashier_id, parent=None):
        super().__init__(parent)
        self.cart = cart
        self.cashier_id = cashier_id
        self.setWindowTitle("Payment")
        layout = QVBoxLayout(self)
        
        self.method = QComboBox()
        self.method.addItems(['cash','mpesa'])
        layout.addWidget(QLabel("Payment Method"))
        layout.addWidget(self.method)
        
        self.mpesa_ref_input = QLineEdit()
        self.mpesa_ref_input.setPlaceholderText("M-Pesa Transaction Code e.g. QAB1C2D3E4")
        layout.addWidget(self.mpesa_ref_input)
        
        btn = QPushButton("Confirm Payment After Checking Phone")
        btn.clicked.connect(self.confirm)
        layout.addWidget(btn)

    def confirm(self):
        order_id, order_no, total = finalize_order(self.cart, self.cashier_id)
        method = self.method.currentText()
        ref = self.mpesa_ref_input.text().strip() if method == 'mpesa' else None
        
        if method == 'mpesa' and not ref:
            QMessageBox.warning(self, "Error", "Enter M-Pesa transaction code")
            return
            
        ok, msg = record_payment(order_id, method, total, ref, self.cashier_id)
        if ok:
            QMessageBox.information(self, "Success", f"Order {order_no} Paid - {msg}")
            self.accept()
        else:
            QMessageBox.critical(self, "Payment Failed", msg)
