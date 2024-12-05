import unittest
from datetime import datetime, timedelta
from auction_system import AuctionSystem
import unittest
from datetime import datetime, timedelta
import unittest
from datetime import datetime, timedelta
from auction_system import AuctionSystem  # Ensure the AuctionSystem class is properly imported

class TestAuctionSystem(unittest.TestCase):
    def setUp(self):
        """Set up an instance of AuctionSystem and register a default user."""
        self.auction_system = AuctionSystem()
        self.auction_system.register_user("test_user", "password123")
        self.auction_system.login_user("test_user", "password123")

    def test_register_user(self):
        """Test user registration."""
        # Register a new user
        result = self.auction_system.register_user("new_user", "new_password")
        self.assertTrue(result)  # Assert that registration is successful
        # Attempt to register an existing user
        result = self.auction_system.register_user("test_user", "password123")
        self.assertFalse(result)  # Assert that duplicate registration fails

    def test_list_item(self):
        """Test listing an item."""
        end_time = (datetime.now() + timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
        # List a valid item
        result = self.auction_system.list_item("Laptop", "A high-end laptop", 500.0, end_time)
        self.assertTrue(result)  # Assert that listing succeeds
        # Attempt to list an item with an invalid end time
        result = self.auction_system.list_item("Laptop", "A high-end laptop", 500.0, "invalid_date")
        self.assertFalse(result)  # Assert that listing fails with invalid date

    def test_place_bid(self):
        """Test placing a bid."""
        end_time = (datetime.now() + timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
        self.auction_system.list_item("Laptop", "A high-end laptop", 500.0, end_time)
        # Place a valid bid
        result = self.auction_system.place_bid("Laptop", 600.0)
        self.assertTrue(result)  # Assert that bid placement succeeds
        # Attempt to place a bid below the minimum price
        result = self.auction_system.place_bid("Laptop", 400.0)
        self.assertFalse(result)  # Assert that bid placement fails for low amount

    def test_display_active_auctions(self):
        """Test displaying active auctions."""
        end_time = (datetime.now() + timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
        self.auction_system.list_item("Laptop", "A high-end laptop", 500.0, end_time)
        # Capture the output of active auctions display
        with self.assertLogs() as captured:
            self.auction_system.display_active_auctions()
        # Ensure that the listed item's details appear in the log
        self.assertIn("Laptop", captured.output[0])

if __name__ == "__main__":
    unittest.main()
