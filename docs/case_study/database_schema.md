# 📂 Database Schema Design (ER Model)

## 1. Users (`users`)
**Why?** Stores customers, agents, and admins.  

**Fields:**
- `id` (PK)  
- `name`  
- `email` (unique)  
- `password`  
- `role` (customer / agent / admin)  
- `phone_number`  
- `created_at`  

---

## 2. Insurers (`insurers`)
**Why?** Stores insurance companies (HDFC, ICICI, etc.)  

**Fields:**
- `id` (PK)  
- `name`  
- `api_url` (integration endpoint)  
- `contact_email`  
- `created_at`  

---

## 3. InsurancePlans (`insurance_plans`)
**Why?** Stores different insurance products from each insurer.  

**Fields:**
- `id` (PK)  
- `insurer_id` (FK → insurers.id)  
- `plan_type` (motor / health / life)  
- `plan_name`  
- `coverage_amount`  
- `premium_base`  
- `created_at`  

---

## 4. Quotes (`quotes`)
**Why?** Stores quotes returned from insurers for customer requests.  

**Fields:**
- `id` (PK)  
- `user_id` (FK → users.id)  
- `plan_id` (FK → insurance_plans.id)  
- `premium_amount`  
- `quote_date`  
- `valid_till`  

---

## 5. Policies (`policies`)
**Why?** Stores purchased policies.  

**Fields:**
- `id` (PK)  
- `user_id` (FK → users.id)  
- `plan_id` (FK → insurance_plans.id)  
- `policy_number` (unique)  
- `premium_amount`  
- `policy_date` (purchase date)  
- `commencement_date` (when coverage starts ✅)  
- `expiry_date`  
- `status` (active / expired / lapsed)  
- `created_at`  

---

## 6. Payments (`payments`)
**Why?** Track transactions for policies.  

**Fields:**
- `id` (PK)  
- `policy_id` (FK → policies.id)  
- `amount`  
- `payment_date`  
- `payment_method` (card, UPI, netbanking)  
- `status` (success / failed / pending)  

---

## 7. Notifications (`notifications`)
**Why?** Track emails/SMS for reminders & confirmations.  

**Fields:**
- `id` (PK)  
- `user_id` (FK → users.id)  
- `policy_id` (FK → policies.id, nullable)  
- `message`  
- `channel` (email / sms)  
- `status` (sent / pending / failed)  
- `sent_at`  

---

# 🔗 Relationships
- **users ↔ quotes ↔ insurance_plans ↔ insurers** (customers receive insurer quotes)  
- **users ↔ policies ↔ payments** (customers buy policies & pay)  
- **policies ↔ notifications** (reminders & confirmations)  


## 📂 Supporting Tables (Future Expansion)

Later, we can add the following tables to make the insurance marketplace more complete and enterprise-ready:

---

### 1. Documents (KYC & Compliance)
**Why?** Customers/agents need to upload ID proofs (PAN, Aadhaar, Driving License).  

**Fields:**
- `id` (PK)  
- `user_id` (FK → Users.id)  
- `document_type` (PAN / Aadhaar / DrivingLicense / Passport)  
- `file_url` (storage path, e.g., S3/Cloud)  
- `verified_status` (pending / verified / rejected)  
- `uploaded_at`  

---

### 2. Nominees / Beneficiaries
**Why?** Required in **life insurance policies** to declare a nominee.  

**Fields:**
- `id` (PK)  
- `policy_id` (FK → Policies.id)  
- `name`  
- `relation` (spouse / child / parent / other)  
- `dob`  
- `contact`  

---

### 3. Claims
**Why?** Customers should be able to raise claims against their policies.  

**Fields:**
- `id` (PK)  
- `policy_id` (FK → Policies.id)  
- `claim_date`  
- `claim_amount`  
- `status` (initiated / under_review / approved / rejected)  
- `settlement_date` (nullable)  

---

### 4. Audit Logs
**Why?** For compliance and tracking user/system actions.  

**Fields:**
- `id` (PK)  
- `user_id` (FK → Users.id)  
- `action` (created_policy, updated_payment, claim_submitted, etc.)  
- `timestamp`  

---

### 5. Locations
**Why?** Insurance plans may vary based on **country / state / city**.  

**Fields:**
- `id` (PK)  
- `country_code` (ISO standard)  
- `country_name`  
- `state_name` (nullable)  
- `city_name` (nullable)  

Relations:  
- `Users` → can store location info  
- `InsurancePlans` → availability by region  

---

### 6. Commissions (For Agents)
**Why?** Agents earn commission on each successful policy sale.  

**Fields:**
- `id` (PK)  
- `agent_id` (FK → Users.id, role = agent)  
- `policy_id` (FK → Policies.id)  
- `commission_amount`  
- `paid_status` (pending / paid)  
- `created_at`  

---
