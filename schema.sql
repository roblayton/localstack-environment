\set db `echo "$ADYN_POSTGRES_DB"`;
\set usr `echo "$ADYN_POSTGRES_USER"`;

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
DROP TABLE GenotypeValues CASCADE;
DROP TABLE HormoneValues CASCADE;
DROP TABLE Shipments CASCADE;
DROP TABLE OrderHistory CASCADE;
DROP TABLE Orders CASCADE;
DROP TABLE MedicalBioSubmissions CASCADE;
DROP TABLE ShippingAddresses CASCADE;
DROP TABLE Customers CASCADE;
DROP TABLE Genotypes CASCADE;
DROP TABLE Hormones CASCADE;

CREATE TABLE IF NOT EXISTS Customers (
  id uuid NOT NULL DEFAULT uuid_generate_v4(),
  email VARCHAR(80) UNIQUE NOT NULL,
  new_email VARCHAR(80) UNIQUE,
  phone VARCHAR(20),
  password_hash VARCHAR(255),
  first_name VARCHAR(80),
  last_name VARCHAR(80),
  preferred_name VARCHAR(80),
  sex VARCHAR(1),
  gender VARCHAR(20),
  pronouns VARCHAR(20),
  date_of_birth DATE,
  zip VARCHAR(45),
  v_code VARCHAR(255),
  v_code_used BOOLEAN DEFAULT False,
  u_code VARCHAR(255),
  u_code_used BOOLEAN DEFAULT True,
  role INTEGER NOT NULL DEFAULT 2,
  -- 0 = admin, 1 = editor, 2 = user/customer, 3 = purchaser, 4 = guest
  status INTEGER NOT NULL DEFAULT 1,
  age_confirmed BOOLEAN DEFAULT False,
  residence_confirmed BOOLEAN DEFAULT False,
  terms_confirmed BOOLEAN DEFAULT False,
  email_pref BOOLEAN NOT NULL DEFAULT True,
  referral_hero_id VARCHAR(45),
  hubspot_id VARCHAR(45),
  hubspot_list INTEGER DEFAULT 0,
  stripe_customer_id VARCHAR(45),
  steadymd_patient_id VARCHAR(45),
  active BOOLEAN NOT NULL DEFAULT True,
  created_date TIMESTAMP NOT NULL,
  modified_date TIMESTAMP,
  ip VARCHAR(45),
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS MedicalBioSubmissions (
  id uuid NOT NULL DEFAULT uuid_generate_v4(),
  jotform_id VARCHAR(45) NOT NULL,
  jotform_form_id VARCHAR(45) NOT NULL,
  customer_id uuid NOT NULL,
  ip VARCHAR(45),
  completion INTEGER,
  elapsed_time INTEGER,
  created_date TIMESTAMP NOT NULL,
  modified_date TIMESTAMP,
  CONSTRAINT fk_customer_id
    FOREIGN KEY (customer_id) 
      REFERENCES Customers(id)
      ON UPDATE CASCADE
      ON DELETE CASCADE,
  UNIQUE(customer_id, jotform_form_id),
  PRIMARY KEY (id, customer_id, jotform_form_id)
);

CREATE TABLE IF NOT EXISTS ShippingAddresses (
  id uuid NOT NULL DEFAULT uuid_generate_v4(),
  customer_id uuid NOT NULL UNIQUE,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  address1 VARCHAR(255) NOT NULL,
  address2 VARCHAR(255),
  city VARCHAR(45) NOT NULL,
  state VARCHAR(2) NOT NULL,
  zip VARCHAR(45) NOT NULL,
  country VARCHAR(2) NOT NULL,
  delivery_instructions TEXT,
  created_date TIMESTAMP NOT NULL,
  modified_date TIMESTAMP,
  CONSTRAINT fk_customer_id
    FOREIGN KEY (customer_id) 
      REFERENCES Customers(id)
      ON UPDATE CASCADE
      ON DELETE CASCADE,
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS Orders (
  id uuid NOT NULL DEFAULT uuid_generate_v4(),
  customer_id uuid NOT NULL,
  stripe_invoice_item_id VARCHAR(45),
  activation_code VARCHAR(45),
  activated BOOLEAN DEFAULT False,
  sku VARCHAR(12),
  package_unit VARCHAR(5),
  package_unit_quantity INTEGER,
  allied_order_number VARCHAR(20),
  allied_order_date TIMESTAMP,
  status VARCHAR(45),
  date_order_placed TIMESTAMP,
  date_order_paid TIMESTAMP,
  status_checked BOOLEAN DEFAULT False,
  ip VARCHAR(45),
  created_date TIMESTAMP NOT NULL,
  modified_date TIMESTAMP,
  PRIMARY KEY (id),
  CONSTRAINT fk_customer
    FOREIGN KEY (customer_id) 
      REFERENCES Customers(id)
      ON UPDATE CASCADE
      ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Shipments (
  id uuid NOT NULL DEFAULT uuid_generate_v4(),
  order_id uuid NOT NULL,
  tracking_number VARCHAR(22),
  date_shipped TIMESTAMP,
  shipped_via VARCHAR(20),
  status VARCHAR(45),
  details TEXT,
  return_tracking_number_1 VARCHAR(22),
  return_tracking_number_2 VARCHAR(22),
  created_date TIMESTAMP NOT NULL,
  modified_date TIMESTAMP,
  status_checked BOOLEAN DEFAULT False,
  PRIMARY KEY (id),
  CONSTRAINT fk_order
    FOREIGN KEY (order_id) 
      REFERENCES Orders(id)
      ON UPDATE CASCADE
      ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS OrderHistory (
  id uuid NOT NULL DEFAULT uuid_generate_v4(),
  order_id UUID NOT NULL,
  field VARCHAR(50) NOT NULL,
  old_value VARCHAR(255) NULL,
  new_value VARCHAR(255) NULL,
  creator uuid NOT NULL,
  created_date TIMESTAMP NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT fk_order
    FOREIGN KEY (order_id) 
      REFERENCES Orders(id)
      ON UPDATE CASCADE
      ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Genotypes (
  id uuid NOT NULL DEFAULT uuid_generate_v4(),
  name VARCHAR(50) NOT NULL,
  chrom INTEGER NOT NULL,
  position INTEGER NOT NULL,
  ref_value VARCHAR(1) NOT NULL,
  alt_value VARCHAR(1) NOT NULL,
  created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  modified_date TIMESTAMP,
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS GenotypeValues (
  id uuid NOT NULL DEFAULT uuid_generate_v4(),
  customer_id uuid NOT NULL,
  genotype_id uuid NOT NULL,
  order_id UUID NOT NULL,
  genotype_value TEXT NOT NULL,
  is_ref BOOLEAN NOT NULL,
  created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  modified_date TIMESTAMP,
  PRIMARY KEY (id),
  CONSTRAINT fk_customer
    FOREIGN KEY (customer_id) 
      REFERENCES Customers(id)
      ON UPDATE CASCADE
      ON DELETE CASCADE,
  CONSTRAINT fk_genotype
    FOREIGN KEY (genotype_id) 
      REFERENCES Genotypes(id)
      ON UPDATE CASCADE
      ON DELETE CASCADE,
  CONSTRAINT fk_order
    FOREIGN KEY (order_id) 
      REFERENCES Orders(id)
      ON UPDATE CASCADE
      ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Hormones (
  id uuid NOT NULL DEFAULT uuid_generate_v4(),
  name VARCHAR(50) NOT NULL,
  ref_high VARCHAR(1) NOT NULL,
  ref_low VARCHAR(1) NOT NULL,
  created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  modified_date TIMESTAMP,
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS HormoneValues (
  id uuid NOT NULL DEFAULT uuid_generate_v4(),
  customer_id uuid NOT NULL,
  hormone_id uuid NOT NULL,
  order_id UUID NOT NULL,
  hormone_value TEXT NOT NULL,
  is_ref BOOLEAN NOT NULL,
  created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  modified_date TIMESTAMP,
  PRIMARY KEY (id),
  CONSTRAINT fk_customer
    FOREIGN KEY (customer_id) 
      REFERENCES Customers(id)
      ON UPDATE CASCADE
      ON DELETE CASCADE,
  CONSTRAINT fk_hormone
    FOREIGN KEY (hormone_id) 
      REFERENCES Hormones(id)
      ON UPDATE CASCADE
      ON DELETE CASCADE,
  CONSTRAINT fk_order
    FOREIGN KEY (order_id) 
      REFERENCES Orders(id)
      ON UPDATE CASCADE
      ON DELETE CASCADE
);
