import os
import pytest
from src.notification.log_alerts import log_alert
from src.notification.send_alerts import send_email_alert

def test_log_alert(tmp_path):
    log_file = tmp_path / "alerts.log"
    
    message = "Teste de alerta de fraude"
    log_alert(message)
    
    with open(log_file, "r") as f:
        log_content = f.read()
    
    assert message in log_content

@pytest.mark.parametrize("email, message", [
    ("test@example.com", "Alerta de fraude detectada!"),
    ("admin@example.com", "Fraude identificada no documento."),
])
def test_send_email_alert(mocker, email, message):
    mock_smtp = mocker.patch("smtplib.SMTP")
    
    send_email_alert(email, message)

    mock_smtp.assert_called_once_with("smtp.example.com", 587)
    instance = mock_smtp.return_value
    instance.login.assert_called_once_with("alerts@example.com", "senha")
    instance.send_message.assert_called_once()
