from pathlib import Path
import sys
import pandas as pd
import numpy as np
from unittest.mock import patch
parent_dir = Path(__file__).resolve().parent.parent

# Add parent directory to sys.path
sys.path.append(str(parent_dir))

from etl.extract import read_products_csv, read_users_excel

class TestExtractFunctions():

    expected_df = pd.DataFrame({
    "product_id": [1],
    "name": ["Apple"],
    "price": [1.99],
    "some_date": pd.to_datetime(["2024-01-01"])
    })
    expected_data_types = {
        "product_id": np.int16,
        "name": 'S10',
        "price": np.float32
    }
    test_path = "test_path_csv"

    @patch("etl.extract.pd.read_csv", return_value=expected_df)
    def test_read_products_csv_success(self, mock_read_csv):
        """Test read_products_csv response"""
        df = read_products_csv(self.test_path)
        pd.testing.assert_frame_equal(df, self.expected_df)
        mock_read_csv.assert_called_once_with(
            self.test_path,
            parse_dates=[3],
            dtype=self.expected_data_types
        )

    @patch("etl.extract.pd.read_csv", side_effect=FileNotFoundError)
    def test_read_products_csv_fail_file_not_found(self, mock_read_csv):
        """Test read_products_csv response"""
        df = read_products_csv(self.test_path)
        mock_read_csv.assert_called_once_with(
            self.test_path,
            parse_dates=[3],
            dtype=self.expected_data_types
        )
        assert df is None