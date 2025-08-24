# 📄 InsureConnect – Requirements & Use Cases

---

## 1. Actors

- **Customer** – buys/renews insurance, uploads docs, makes payments.  
- **Agent** – helps customers get best policy (future extension).  
- **Insurer (Adapter)** – external insurance providers (HDFC, ICICI, PNBMetLife).  
- **System Services** – Payment Gateway, Document Service, Notification Service.  

---

## 2. Core Use Cases

### UC1: Customer Registration & Login
- Customer registers with **name, email, phone, password**.  
- Login with credentials.  
- Update profile.  

---

### UC2: Get Quotes
- Customer selects insurance type (**Motor, Health, Life**).  
- System sends request to multiple insurers (**via Adapters**).  
- Quotes are returned.  
- Customer compares quotes.  

---

### UC3: Buy Policy
- Customer selects a quote.  
- Uploads necessary documents.  
- Makes payment.  
- Policy is generated and stored.  
- Notification sent to customer.  

---

### UC4: Document Upload
- Customer uploads documents (e.g., **RC for motor, medical docs for health, KYC for life**).  
- Document validation (**basic checks**).  
- Storage in system.  

---

### UC5: Payment Processing
- Customer initiates payment.  
- System calls **Payment Gateway** (mock first).  
- Payment is verified.  
- **On success** → Issue policy & notify customer.  
- **On failure** → Send error notification.  

---

### UC6: Notifications
- System sends **Email / SMS / Push** for:  
  - Registration success.  
  - Payment confirmation.  
  - Policy issued.  
  - Renewal reminders.  

---

### UC7: Policy Management
- View active policies.  
- Download policy documents.  
- Renew expired policy.  

---

## 3. Non-Functional Requirements
- **Secure** → HTTPS, JWT authentication.  
- **Scalable** → can add insurers easily.  
- **Extensible** → support for new insurance types.  
- **Cloud-ready** → Docker + AWS ECS deployment.  

---
