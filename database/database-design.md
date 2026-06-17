# Database Design

## Main Entities

### Customers

- customer_id
- full_name
- contact_information
- status

### Providers

- provider_id
- company_name
- category
- rating
- status

### Services

- service_id
- provider_id
- service_name
- category
- price

### Bookings

- booking_id
- customer_id
- provider_id
- booking_date
- status

### Reviews

- review_id
- booking_id
- rating
- feedback

### AI Recommendations

- recommendation_id
- customer_id
- generated_date
- recommendation_type

### Marketplace Analytics

- analytics_id
- metric_name
- value
- generated_date

---

## Technologies

- PostgreSQL
- MySQL
- Supabase
- Firebase

---

## Future Expansion

- recommendation graph
- dynamic pricing
- reputation engine
- fraud detection
- provider intelligence
