import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { UserForm } from './components/user_form/_user_form';
import { LogIn } from './components/log_in/_log_in';
import { NotFound } from './components/errors/not_found';
import { AvailabilitySelector } from './components/availability_selector/availability_selector';
import { LoadingAvailability } from './components/availability_selector/loading';
import { About } from './components/about_page/about';
import { JobForm } from './components/job_form/job_form';
import { JobsPage } from './components/jobs_page/jobs_page';
import { ContactForm } from './components/contactform/contact_form';
import { ViewAllUsers } from './components/owner_portal/view_all_users';
import { ViewContactForms } from './components/owner_portal/view_contact_forms';
import { OwnerPortal } from './components/owner_portal/owner_portal';
import { JobView } from './components/job_view/_job_view';
import { ViewAllJobs } from './components/owner_portal/view_all_jobs';
import { ManageJobTypes } from './components/owner_portal/job_types/manage_job_types';
import { JobTypeForm } from './components/owner_portal/job_types/job_type_form';
import { Home } from './components/home/_home';


ReactDOM.render(
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<App />} >
        <Route path="/" element={<Home />} />       

        <Route path="signup" element={<UserForm newUser={true} />} />
        <Route path="profile/:id/edit" element={<UserForm newUser={false} />} />
        <Route path="worker/:id/availability" element={<AvailabilitySelector />} />
        <Route path="worker/load-availability" element={<LoadingAvailability />} />
        <Route path="login" element={<LogIn />} />

        <Route path="about" element={<About />} />
        <Route path="contact" element={<ContactForm />} />
        <Route path="contact/dispute/:id" element={<ContactForm />} />

        <Route path="jobs" element={<JobsPage />} />
        <Route path="jobs/add-job" element={<JobForm newJob={true} />} />
        <Route path="job/:id/edit" element={<JobForm />} />
        <Route path="job/:id" element={<JobView />} />

        <Route path="owner/view-users" element={<ViewAllUsers/>} />
        <Route path="owner/view-jobs" element={<ViewAllJobs/>} />
        <Route path="owner/view-forms" element={<ViewContactForms/>} />
        <Route path="owner/manage-job-types" element={<ManageJobTypes/>} />
        <Route path="owner/manage-job-types/add" element={<JobTypeForm />} />
        <Route path="owner/portal" element={<OwnerPortal/>} />

        <Route
          path="*"
          element={<NotFound />}
        />
      </Route>
    </Routes>
  </BrowserRouter>,
  document.getElementById('root')
);
