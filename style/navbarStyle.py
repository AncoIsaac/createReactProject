NAVBAR_CSS = """"
.navbar {
  background: linear-gradient(90deg, #5c9ea0, #326ea7, #5f628b);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.notificationBtn {
  background: rgba(222, 235, 238, 0.753);
  backdrop-filter: blur(10px);
  transition: all 0.3s ease;
}

.notificationBtn:hover {
  background: rgba(14, 133, 127, 0.986);
}

.notificationBadge {
  position: absolute;
  background-color: red;
  top: -0.10rem;
  right: -0.13rem;
  color: white;
  font-size: 0.75rem;
  border-radius: 9999px;
  height: .9rem;
  width: .9rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.logoutButton {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background-color: #61c3d4; /* amber-500 */
  padding: 0.1rem 1rem;
  border-radius: 0.5rem;
  transition: background-color 0.2s;
}

.logoutButton:hover {
  background: rgba(14, 133, 127, 0.986);
}

.notificationsDropdown {
  position: absolute;
  right: 14px;
  top: 110%;
  width: 320px;
  background: white;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  z-index: 1000;
  color: #333;
}

.notificationsHeader {
  padding: 12px 16px;
  border-bottom: 1px solid #eee;
}

.notificationsHeader h3 {
  margin: 0;
  font-size: 14px;
  font-weight: 600;
}

.notificationsList {
  max-height: 400px;
  overflow-y: auto;
}

.notificationItem {
  padding: 12px 16px;
  border-bottom: 1px solid #eee;
  transition: background 0.2s;
}

.notificationItem:hover {
  background: #f9f9f9;
}

.notificationItem p {
  margin: 0 0 4px 0;
  font-size: 14px;
}

.notificationItem small {
  color: #666;
  font-size: 12px;
}

.notificationsFooter {
  padding: 8px 16px;
  text-align: center;
  border-top: 1px solid #eee;
}

.notificationsFooter button {
  background: none;
  border: none;
  color: #2563eb;
  cursor: pointer;
  font-size: 13px;
}
"""
