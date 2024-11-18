## **1. Dashboard**

**Purpose:** Provide an overview of the company's operations and key metrics.

**Components:**

- **Summary Cards:**

  - Total Offices
  - Total Staff
  - Total Owners
  - Total Drivers
  - Total Taxis
  - Total Contracts
  - Total Clients
  - Active Jobs

- **Recent Activity Feed:**
  - Recently Completed Jobs
  - New Bookings
  - Alerts (e.g., Failed Jobs)

---

## **2. Office Management**

### **a. Office List Page (`/offices`)**

**Purpose:** Display all offices with options to view, edit, or delete.

**Components:**

- **Table Columns:**

  - Office ID
  - Phone Number
  - Address (Street, City)
  - Actions: View, Edit, Delete

- **Buttons:**
  - Add New Office (`/offices/new`)

### **b. Office Details Page (`/offices/[id]`)**

**Purpose:** Display detailed information about a specific office.

**Components:**

- **Office Information:**

  - Office ID
  - Phone Number
  - Full Address

- **Tabs/Sections:**

  - **Staff Assigned:** List of staff members with roles and contact info.
  - **Owners Associated:** List of owners linked to this office.
  - **Drivers Associated:** List of drivers operating from this office.
  - **Taxis Operating:** List of taxis available at this office.
  - **Contracts Associated:** List of contracts managed by this office.

- **Actions:**
  - Edit Office (`/offices/[id]/edit`)
  - Delete Office (Confirmation modal)

### **c. Office Create/Edit Form (`/offices/new` or `/offices/[id]/edit`)**

**Purpose:** Add a new office or edit an existing one.

**Form Fields:**

- **Phone Number:** Input field
- **Address:**

  - **Select Existing Address:** Dropdown
  - **Or Add New Address:**
    - Street: Input field
    - City: Input field
    - Postcode: Input field
    - Country: Input field

- **Buttons:**
  - Save
  - Cancel

---

## **3. Staff Management**

### **a. Staff List Page (`/staff`)**

**Purpose:** Display all staff members with options to view, edit, or delete.

**Components:**

- **Table Columns:**

  - Staff ID
  - Name
  - Role
  - Office
  - Actions: View, Edit, Delete

- **Buttons:**
  - Add New Staff Member (`/staff/new`)

### **b. Staff Details Page (`/staff/[id]`)**

**Purpose:** Display detailed information about a specific staff member.

**Components:**

- **Personal Information:**

  - Name
  - Gender
  - Date of Birth
  - Phone Number

- **Professional Information:**

  - Staff ID
  - Role
  - NIN (National Insurance Number)
  - Office Assigned

- **Actions:**
  - Edit Staff Member (`/staff/[id]/edit`)
  - Delete Staff Member (Confirmation modal)

### **c. Staff Create/Edit Form (`/staff/new` or `/staff/[id]/edit`)**

**Purpose:** Add a new staff member or edit an existing one.

**Form Fields:**

- **User Information:**

  - **Select Existing User:** Dropdown
  - **Or Add New User:**
    - Name: Input field
    - Gender: Dropdown
    - Date of Birth: Date picker
    - Phone Number: Input field
    - Address: (Same as in Office Form)

- **Professional Information:**

  - Office: Dropdown
  - Role: Input field
  - NIN: Input field

- **Buttons:**
  - Save
  - Cancel

---

## **4. Owner Management**

### **a. Owner List Page (`/owners`)**

**Purpose:** Display all taxi owners with options to view, edit, or delete.

**Components:**

- **Table Columns:**

  - Owner ID
  - Name
  - NIN
  - Office
  - Actions: View, Edit, Delete

- **Buttons:**
  - Add New Owner (`/owners/new`)

### **b. Owner Details Page (`/owners/[id]`)**

**Purpose:** Display detailed information about a specific owner.

**Components:**

- **Personal Information:**

  - Name
  - Gender
  - Date of Birth
  - Phone Number
  - NIN

- **Professional Information:**

  - Owner ID
  - Office Associated

- **Assets:**

  - **Taxis Owned:** List with registration numbers and capacities.
  - **Drivers Associated:** List of drivers linked to the owner's taxis.

- **Actions:**
  - Edit Owner (`/owners/[id]/edit`)
  - Delete Owner (Confirmation modal)

### **c. Owner Create/Edit Form (`/owners/new` or `/owners/[id]/edit`)**

**Purpose:** Add a new owner or edit an existing one.

**Form Fields:**

- **User Information:** (Same as in Staff Form)
- **Professional Information:**

  - Office: Dropdown
  - NIN: Input field

- **Buttons:**
  - Save
  - Cancel

---

## **5. Driver Management**

### **a. Driver List Page (`/drivers`)**

**Purpose:** Display all drivers with options to view, edit, or delete.

**Components:**

- **Table Columns:**

  - Driver ID
  - Name
  - Licence Number
  - Taxi Assigned
  - Actions: View, Edit, Delete

- **Buttons:**
  - Add New Driver (`/drivers/new`)

### **b. Driver Details Page (`/drivers/[id]`)**

**Purpose:** Display detailed information about a specific driver.

**Components:**

- **Personal Information:**

  - Name
  - Gender
  - Date of Birth
  - Phone Number
  - NIN
  - Licence Number
  - Join Date

- **Professional Information:**

  - Driver ID
  - Owner (if applicable)
  - Taxi Assigned

- **Job History:**

  - List of jobs assigned with status and dates.

- **Actions:**
  - Edit Driver (`/drivers/[id]/edit`)
  - Delete Driver (Confirmation modal)

### **c. Driver Create/Edit Form (`/drivers/new` or `/drivers/[id]/edit`)**

**Purpose:** Add a new driver or edit an existing one.

**Form Fields:**

- **User Information:** (Same as in Staff Form)
- **Professional Information:**

  - Owner: Dropdown (Can be left empty if the driver is not an owner)
  - NIN: Input field
  - Licence Number: Input field
  - Join Date: Date picker
  - Taxi: Dropdown

- **Buttons:**
  - Save
  - Cancel

---

## **6. Taxi Management**

### **a. Taxi List Page (`/taxis`)**

**Purpose:** Display all taxis with options to view, edit, or delete.

**Components:**

- **Table Columns:**

  - Taxi ID
  - Registration Number
  - Capacity
  - Owner
  - Actions: View, Edit, Delete

- **Buttons:**
  - Add New Taxi (`/taxis/new`)

### **b. Taxi Details Page (`/taxis/[id]`)**

**Purpose:** Display detailed information about a specific taxi.

**Components:**

- **Taxi Information:**

  - Taxi ID
  - Registration Number
  - Capacity
  - Owner Details

- **Assigned Drivers:**

  - List of drivers who operate this taxi.

- **Actions:**
  - Edit Taxi (`/taxis/[id]/edit`)
  - Delete Taxi (Confirmation modal)

### **c. Taxi Create/Edit Form (`/taxis/new` or `/taxis/[id]/edit`)**

**Purpose:** Add a new taxi or edit an existing one.

**Form Fields:**

- **Owner:** Dropdown
- **Registration Number:** Input field
- **Capacity:** Input field

- **Buttons:**
  - Save
  - Cancel

---

## **7. Client Management**

### **a. Client List Page (`/clients`)**

**Purpose:** Display all clients (private and business) with options to view, edit, or delete.

**Components:**

- **Table Columns:**

  - Client ID
  - Client Type (Private/Business)
  - Name or Business Name
  - Actions: View, Edit, Delete

- **Buttons:**
  - Add New Private Client (`/clients/private/new`)
  - Add New Business Client (`/clients/business/new`)

### **b. Client Details Page (`/clients/[id]`)**

**Purpose:** Display detailed information about a specific client.

**Components:**

- **For Private Clients:**

  - **Personal Information:**

    - Name
    - Gender
    - Date of Birth
    - Phone Number
    - Join Date

  - **Job History:**
    - List of jobs with status and dates.

- **For Business Clients:**

  - **Business Information:**

    - Business Client ID
    - HST Number
    - Address

  - **Contracts:**

    - List of contracts with details.

  - **Job History:**
    - List of jobs linked to contracts.

- **Actions:**
  - Edit Client (`/clients/[id]/edit`)
  - Delete Client (Confirmation modal)

### **c. Private Client Create/Edit Form (`/clients/private/new` or `/clients/private/[id]/edit`)**

**Purpose:** Add a new private client or edit an existing one.

**Form Fields:**

- **User Information:** (Same as in Staff Form)
- **Join Date:** Date picker

- **Buttons:**
  - Save
  - Cancel

### **d. Business Client Create/Edit Form (`/clients/business/new` or `/clients/business/[id]/edit`)**

**Purpose:** Add a new business client or edit an existing one.

**Form Fields:**

- **Business Information:**

  - HST Number: Input field
  - Address: (Same as in Office Form)

- **Contact Information:**

  - Primary Contact Name: Input field
  - Phone Number: Input field
  - Email: Input field

- **Buttons:**
  - Save
  - Cancel

---

## **8. Contract Management**

### **a. Contract List Page (`/contracts`)**

**Purpose:** Display all contracts with options to view, edit, or delete.

**Components:**

- **Table Columns:**

  - Contract ID
  - Office
  - Business Client
  - Signed On
  - Number of Jobs
  - Flat Fees
  - Actions: View, Edit, Delete

- **Buttons:**
  - Add New Contract (`/contracts/new`)

### **b. Contract Details Page (`/contracts/[id]`)**

**Purpose:** Display detailed information about a specific contract.

**Components:**

- **Contract Information:**

  - Contract ID
  - Office Details
  - Business Client Details
  - Signed On Date
  - Number of Jobs
  - Flat Fees

- **Associated Jobs:**

  - List of jobs under this contract.

- **Actions:**
  - Edit Contract (`/contracts/[id]/edit`)
  - Delete Contract (Confirmation modal)

### **c. Contract Create/Edit Form (`/contracts/new` or `/contracts/[id]/edit`)**

**Purpose:** Add a new contract or edit an existing one.

**Form Fields:**

- **Office:** Dropdown
- **Business Client:** Dropdown
- **Signed On Date:** Date picker
- **Number of Jobs:** Input field
- **Flat Fees:** Input field

- **Buttons:**
  - Save
  - Cancel

---

## **9. Job Management**

### **a. Job List Page (`/jobs`)**

**Purpose:** Display all jobs with options to view, edit, or delete.

**Components:**

- **Table Columns:**

  - Job ID
  - Client Name
  - Driver Name
  - Pickup Date/Time
  - Status
  - Actions: View, Edit, Delete

- **Filters:**

  - Status Dropdown (All, Pending, Assigned, Completed, Failed)
  - Date Range Picker

- **Buttons:**
  - Add New Job (`/jobs/new`)

### **b. Job Details Page (`/jobs/[id]`)**

**Purpose:** Display detailed information about a specific job.

**Components:**

- **Job Information:**

  - Job ID
  - Client Details
  - Driver Details
  - Contract (if applicable)
  - Mileage
  - Charge
  - Status
  - Failure Reason (if any)
  - Pickup Date/Time
  - Drop-off Date/Time
  - Pickup Address
  - Drop-off Address (if different)

- **Actions:**
  - Edit Job (`/jobs/[id]/edit`)
  - Update Status (`/jobs/[id]/update`)
  - Delete Job (Confirmation modal)

### **c. Job Create/Edit Form (`/jobs/new` or `/jobs/[id]/edit`)**

**Purpose:** Add a new job or edit an existing one.

**Form Fields:**

- **Client Information:**

  - **Select Existing Client:** Dropdown
  - **Or Add New Client:** Link to client creation page

- **Driver Assignment:**

  - **Assign Automatically:** Checkbox
  - **Or Select Driver:** Dropdown

- **Contract:** Dropdown (Optional, only for business clients)

- **Job Details:**

  - Pickup Date/Time: DateTime picker
  - Drop-off Date/Time: DateTime picker (Optional)
  - Pickup Address: (Same as in Office Form)
  - Drop-off Address: (Optional)
  - Status: Dropdown (Default to 'Pending')

- **Buttons:**
  - Save
  - Cancel

### **d. Job Update Form (`/jobs/[id]/update`)**

**Purpose:** Update job status and completion details.

**Form Fields:**

- **Mileage:** Input field
- **Charge:** Input field (For private clients only)
- **Status:** Dropdown (Completed, Failed)
- **Failure Reason:** Textarea (Required if status is 'Failed')

- **Buttons:**
  - Update
  - Cancel

---

## **10. User Management**

### **a. User List Page (`/users`)**

**Purpose:** Display all users with options to view, edit, or delete.

**Components:**

- **Table Columns:**

  - User ID
  - Name
  - Phone Number
  - Actions: View, Edit, Delete

- **Buttons:**
  - Add New User (`/users/new`)

### **b. User Details Page (`/users/[id]`)**

**Purpose:** Display detailed information about a specific user.

**Components:**

- **Personal Information:**

  - Name
  - Gender
  - Date of Birth
  - Phone Number
  - Address

- **Associated Roles:**

  - Indicates if the user is a Staff Member, Owner, Driver, or Private Client.

- **Actions:**
  - Edit User (`/users/[id]/edit`)
  - Delete User (Confirmation modal)

### **c. User Create/Edit Form (`/users/new` or `/users/[id]/edit`)**

**Purpose:** Add a new user or edit an existing one.

**Form Fields:**

- **Name:** Input field
- **Gender:** Dropdown
- **Date of Birth:** Date picker
- **Phone Number:** Input field
- **Address:** (Same as in Office Form)

- **Buttons:**
  - Save
  - Cancel

---

## **11. Address Management**

### **a. Address Create/Edit Form**

**Purpose:** Used within other forms to add or edit an address.

**Form Fields:**

- **Street:** Input field
- **City:** Input field
- **Postcode:** Input field
- **Country:** Input field

- **Buttons:**
  - Save
  - Cancel

---

## **Navigation Structure**

- **Main Navigation Bar:**

  - Dashboard
  - Offices
  - Staff
  - Owners
  - Drivers
  - Taxis
  - Clients
  - Contracts
  - Jobs
  - Users
  - Reports (Optional)

- **User Account Menu:**
  - Profile
  - Settings
  - Logout
