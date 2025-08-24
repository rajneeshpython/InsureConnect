# 📌 Step 1 – Requirements for InsureConnect

## 🎯 Primary Goal
Build a multi-insurance aggregator platform where users can compare and purchase policies for **Life, Motor, and Health insurance** from different insurers (HDFC Life, ICICI Lombard, PNB MetLife, etc.).

---

## 🧑‍🤝‍🧑 Actors
- **Customer (User):** Person buying the policy.  
- **Aggregator System (InsureConnect):** Our platform.  
- **Insurers (External APIs):** HDFC, ICICI, PNB MetLife, etc.  
- **Admin:** Internal team managing insurers, plans, and monitoring.  

---

## ✅ Functional Requirements

### 1. User Management
- Register, login, and profile management.  
- Upload and manage KYC documents.  

### 2. Policy Modules
- Life Insurance  
- Health Insurance  
- Motor Insurance  

### 3. Quote Engine
- User enters details.  
- Fetches quotes from multiple insurers (via APIs).  

### 4. Policy Purchase
- Redirect to insurer **OR** complete purchase on InsureConnect (if supported).  

### 5. Payment Handling
- Mock gateway integration with callback support.  

### 6. Policy Management
- View purchased policies.  
- Download policy documents.  

### 7. Notifications
- Email/SMS for purchase confirmation.  
- Renewal reminders.  

---

## 🔒 Non-Functional Requirements
- **Scalability:** Handle high concurrent quote requests.  
- **Reliability:** No quote loss if insurer API fails → implement retry/queue.  
- **Security:** JWT-based authentication, encrypted sensitive data.  
- **Extensibility:** Easy to add new insurers.  
- **Logging & Monitoring:** Audit logs, error monitoring.  

---

## 🚘 Supported Insurance Types (Phase 1)
- **Life Insurance:** Term Life plans.  
- **Motor Insurance:** Car, Two-wheeler insurance.  
- **Health Insurance:** Family Floater, Individual Health.  

---

## 🏦 Insurers to Integrate
- HDFC Life (Life)  
- ICICI Lombard (Health & Motor)  
- PNB MetLife (Life)  
- Star Health (Health)  
- Bajaj Allianz (Motor)  

---

## 📚 Real-time Use Cases
1. Customer wants **Car Insurance** → enters car details → system fetches premiums from ICICI & Bajaj → compares → purchases.  
2. Customer buys **Health Plan** → selects Star Health → makes payment → receives policy PDF.  
3. Customer wants **Term Life Insurance** → checks HDFC Life & PNB MetLife → picks cheapest premium.  
4. **System Failure Case** → if ICICI API is down, still show results from other insurers.  
