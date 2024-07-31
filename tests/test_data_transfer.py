import unittest
from unittest.mock import patch, MagicMock
from src.app.data_transfer import transfer_files

class TestSFTPTransfer(unittest.TestCase):
    
    @patch('src.app.data_transfer.Transport')
    @patch('src.app.data_transfer.SFTPClient.from_transport')
    def test_transfer_files(self, mock_sftp_client, mock_transport):

        mock_transport_instance = MagicMock()
        mock_transport.return_value = mock_transport_instance
        
        mock_sftp_instance = MagicMock()
        mock_sftp_client.return_value = mock_sftp_instance
        
        file_to_transfer = 'dummy_file.txt'
        name_of_file = 'remote_dummy_file.txt'
        
        with patch.dict('os.environ', {
            'SFTP_HOST': 'localhost',
            'SFTP_PORT': '22',
            'SFTP_USER': 'user',
            'SFTP_PASSWORD': 'password'
        }):

            transfer_files(file_to_transfer, name_of_file)
        
        mock_transport.assert_called_once_with(('localhost', 22))
        mock_transport_instance.connect.assert_called_once_with(username='user', password='password')
        
        mock_sftp_client.assert_called_once_with(mock_transport_instance)
        mock_sftp_instance.put.assert_called_once_with(file_to_transfer, './' + name_of_file)
        
        mock_sftp_instance.close.assert_called_once()
        mock_transport_instance.close.assert_called_once()
        
if __name__ == '__main__':
    unittest.main()
