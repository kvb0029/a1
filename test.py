import unittest
from datetime import datetime, timedelta
from auction_system import AuctionSystem
import unittest
from datetime import datetime, timedelta

class TestAuctionSystem(unittest.TestCase):
    def setUp(self):
        """Set up an instance of AuctionSystem and a default user."""
        self.auction_system = AuctionSystem()
        self.auction_system.register_user("test_user", "password123")
        self.auction_system.login_user("test_user", "password123")

    # Your test cases here...

if __name__ == "__main__":
    unittest.main()


class TestAuctionSystem(unittest.TestCase):
    def setUp(self):
        """Set up an instance of AuctionSystem and a default user."""
        self.auction_system = AuctionSystem()
        self.auction_system.register_user("test_user", "password123")
        self.auction_system.login_user("test_user", "password123")

    def test_register_user(self):
        """Test user registration."""
        self.assertTrue(self.auction_system.register_user("new_user", "new_password"))
        self.assertFalse(self.auction_system.register_user("test_user", "password123"))

    def test_login_user(self):
        """Test user login."""
        self.assertTrue(self.auction_system.login_user("test_user", "password123"))
        self.assertFalse(self.auction_system.login_user("test_user", "wrong_password"))
        self.assertFalse(self.auction_system.login_user("nonexistent_user", "password123"))

    def test_list_item(self):
        """Test listing an item."""
        end_time = (datetime.now() + timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
        self.assertTrue(self.auction_system.list_item("Laptop", "A high-end laptop", 500.0, end_time))
        self.assertFalse(self.auction_system.list_item("Laptop", "A high-end laptop", 500.0, "invalid_date"))

    def test_place_bid(self):
        """Test placing a bid."""
        end_time = (datetime.now() + timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
        self.auction_system.list_item("Laptop", "A high-end laptop", 500.0, end_time)
        self.assertTrue(self.auction_system.place_bid("Laptop", 600.0))
        self.assertFalse(self.auction_system.place_bid("Laptop", 400.0))  # Less than min price
        self.assertFalse(self.auction_system.place_bid("Nonexistent Item", 700.0))

    def test_display_active_auctions(self):
        """Test displaying active auctions."""
        end_time = (datetime.now() + timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
        self.auction_system.list_item("Laptop", "A high-end laptop", 500.0, end_time)
        self.auction_system.display_active_auctions()

    def test_display_winners(self):
        """Test displaying auction winners."""
        end_time = (datetime.now() + timedelta(seconds=1)).strftime('%Y-%m-%d %H:%M:%S')
        self.auction_system.list_item("Laptop", "A high-end laptop", 500.0, end_time)
        self.auction_system.place_bid("Laptop", 600.0)
        # Wait for the auction to close
        import time
        time.sleep(2)
        self.auction_system.display_winners()

    def test_search_items(self):
        """Test searching for items."""
        end_time = (datetime.now() + timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
        self.auction_system.list_item("Laptop", "A high-end laptop", 500.0, end_time)
        self.auction_system.search_items("Laptop")
        self.auction_system.search_items("Nonexistent")

    def test_delete_item(self):
        """Test deleting an item."""
        end_time = (datetime.now() + timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
        self.auction_system.list_item("Laptop", "A high-end laptop", 500.0, end_time)
        self.assertTrue(self.auction_system.delete_item("Laptop"))
        self.assertFalse(self.auction_system.delete_item("Nonexistent"))

    def test_update_min_price(self):
        """Test updating the minimum price of an item."""
        end_time = (datetime.now() + timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
        self.auction_system.list_item("Laptop", "A high-end laptop", 500.0, end_time)
        self.assertTrue(self.auction_system.update_min_price("Laptop", 600.0))
        self.assertFalse(self.auction_system.update_min_price("Nonexistent", 700.0))

    def test_view_profile(self):
        """Test viewing user profile."""
        end_time = (datetime.now() + timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
        self.auction_system.list_item("Laptop", "A high-end laptop", 500.0, end_time)
        self.auction_system.view_profile()

    def test_auction_statistics(self):
        """Test auction statistics."""
        end_time = (datetime.now() + timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
        self.auction_system.list_item("Laptop", "A high-end laptop", 500.0, end_time)
        self.auction_system.place_bid("Laptop", 600.0)
        self.auction_system.auction_statistics()

    def test_close_expired_auctions(self):
        """Test closing expired auctions."""
        end_time = (datetime.now() + timedelta(seconds=1)).strftime('%Y-%m-%d %H:%M:%S')
        self.auction_system.list_item("Laptop", "A high-end laptop", 500.0, end_time)
        # Wait for the auction to close
        import time
        time.sleep(2)
        self.auction_system.close_expired_auctions()

    def test_send_message_and_view_messages(self):
        """Test sending and viewing messages."""
        self.auction_system.register_user("another_user", "password456")
        self.assertTrue(self.auction_system.send_message("another_user", "Hello!"))
        self.auction_system.login_user("another_user", "password456")
        self.auction_system.view_messages()

if __name__ == "__main__":
    unittest.main()
