<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Vumatel Installation System</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.installation-modal>Add Installation</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">customer_name</th>
              <th scope="col">Address</th>
              <th scope="col">Appointment_date</th>
              <th scope="col">Created_date</th>
              <th scope="col">Modified_date</th>
              <th scope="col">Status</th>
              <th scope="col">Read?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(installation, index) in installations" :key="index">
              <td>{{ installation.customer_name }}</td>
              <td>{{ installation.Address }}</td>
              <td>{{ installation.Appointment_date }}</td>
              <td>{{ installation.Created_date }}</td>
              <td>{{ installation.Modified_date }}</td>
              <td>{{ installation.Status }}</td>
              <td>
                <span v-if="installation.read">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button
                          type="button"
                          class="btn btn-warning btn-sm"
                          v-b-modal.installation-update-modal
                          @click="editinstallation(installation)">
                      Update
                  </button>
                  <button
                          type="button"
                          class="btn btn-danger btn-sm"
                          @click="onDeleteinstallation(installation)">
                      Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addinstallationModal"
            id="installation-modal"
            title="Add an Installation"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-title-group"
                    label="customer_name:"
                    label-for="form-customer_name-input">
          <b-form-input id="form-customer_name-input"
                        type="text"
                        v-model="addinstallationForm.customer_name"
                        required
                        placeholder="Enter customer_name">
          </b-form-input>
        </b-form-group>

        <b-form-group id="form-customer_name-group"
                      label="Address:"
                      label-for="form-Address-input">
            <b-form-input id="form-Address-input"
                          type="text"
                          v-model="addinstallationForm.Address"
                          required
                          placeholder="Enter Address">
            </b-form-input>
          </b-form-group>


        <b-form-group id="form-Appointment_date-group"
                      label="Appointment_date:"
                      label-for="form-Appointment_date-input">
            <b-form-input id="form-Appointment_date-input"
                          type="text"
                          v-model="addinstallationForm.Appointment_date"
                          required
                          placeholder="Enter Appointment_date">
            </b-form-input>
          </b-form-group>


          <b-form-group id="form-Created_date-group"
                      label="Created_date:"
                      label-for="form-Created_date-input">
            <b-form-input id="form-Created_date-input"
                          type="text"
                          v-model="addinstallationForm.Created_date"
                          required
                          placeholder="Enter Created_date">
            </b-form-input>
          </b-form-group>

          <b-form-group id="form-Modified_date-group"
                      label="Modified_date:"
                      label-for="form-Modified_date-input">
            <b-form-input id="form-Modified_date-input"
                          type="text"
                          v-model="addinstallationForm.Modified_date"
                          required
                          placeholder="Enter Modified_date">
            </b-form-input>
          </b-form-group>

          <b-form-group id="form-Status-group"
                      label="Status:"
                      label-for="form-Status-input">
            <b-form-input id="form-Status-input"
                          type="text"
                          v-model="addinstallationForm.Status"
                          required
                          placeholder="Enter Status">
            </b-form-input>
          </b-form-group>


        <b-form-group id="form-read-group">
          <b-form-checkbox-group v-model="addinstallationForm.read" id="form-checks">
            <b-form-checkbox value="true">Read?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal ref="editinstallationModal"
            id="installation-update-modal"
            title="Update"
            hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
      <b-form-group id="form-customer_name-group"
                    label="customer_name:"
                    label-for="form-customer_name-input">
          <b-form-input id="form-customer_name-input"
                        type="text"
                        v-model="addinstallationForm.customer_name"
                        required
                        placeholder="Enter customer_name">
          </b-form-input>
        </b-form-group>

        <b-form-group id="form-Address-group"
                      label="Address:"
                      label-for="form-Address-input">
            <b-form-input id="form-Address-input"
                          type="text"
                          v-model="addinstallationForm.Address"
                          required
                          placeholder="Enter Address">
            </b-form-input>
          </b-form-group>


        <b-form-group id="form-Appointment_date-group"
                      label="Appointment_date:"
                      label-for="form-Appointment_date-input">
            <b-form-input id="form-Appointment_date-input"
                          type="text"
                          v-model="addinstallationForm.Appointment_date"
                          required
                          placeholder="Enter Appointment_date">
            </b-form-input>
          </b-form-group>


          <b-form-group id="form-Created_date-group"
                      label="Created_date:"
                      label-for="form-Created_date-input">
            <b-form-input id="form-Created_date-input"
                          type="text"
                          v-model="addinstallationForm.Created_date"
                          required
                          placeholder="Enter Created_date">
            </b-form-input>
          </b-form-group>

           <b-form-group id="form-Modified_date-group"
                      label="Modified_date:"
                      label-for="form-Modified_date-input">
            <b-form-input id="form-Modified_date-input"
                          type="text"
                          v-model="addinstallationForm.Modified_date"
                          required
                          placeholder="Enter Modified_date">
            </b-form-input>
          </b-form-group>

           <b-form-group id="form-Status-group"
                      label="Status:"
                      label-for="form-Status-input">
            <b-form-input id="form-Status-input"
                          type="text"
                          v-model="addinstallationForm.Status"
                          required
                          placeholder="Enter Status">
            </b-form-input>
          </b-form-group>

        <b-form-group id="form-read-edit-group">
          <b-form-checkbox-group v-model="editForm.read" id="form-checks">
            <b-form-checkbox value="true">Read?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  data() {
    return {
     installations: [],
      addinstallationForm: {
        customer_name: '',
        Address: '',
        Appointment_date: '',
        Created_date: '',
        Modified_date: '',
        Status: '',
        Read: '',
      },
      message: '',
      showMessage: false,
      editForm: {
        id: '',
        customer_name: '',
        Address:'',
        Appointment_date: '',
        Created_date: '',
        Modified_date: '',
        Status: '',
        Read: '',
      },
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getinstallations() {
      const path = 'http://localhost:5000/installations';
      axios.get(path)
        .then((res) => {
          this.installations = res.data.installations;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addinstallation(payload) {
      const path = 'http://localhost:5000/installations';
      axios.post(path, payload)
        .then(() => {
          this.getinstallations();
          this.message = 'Installation added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getinstallations();
        });
    },
    initForm() {
      this.addinstallationForm.customer_name = '';
      this.addinstallationForm.Address = '';
      this.addinstallationForm.Appointment_date = '';
      this.addinstallationForm.Created_date = '';
      this.addinstallationForm.Modified_date = '';
      this.addinstallationForm.Status = '';
      this.addinstallationForm.read = [];
      this.editForm.id = '';

      this.addinstallationForm.customer_name = '';
      this.addinstallationForm.Address = '';
      this.addinstallationForm.Appointment_date = '';
      this.addinstallationForm.Created_date = '';
      this.addinstallationForm.Modified_date = '';
      this.addinstallationForm.Status = '';
      this.addinstallationForm.read = [];
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addinstallationModal.hide();
      let read = false;
      if (this.addinstallationForm.read[0]) read = true;
      const payload = {
        customer_name: this.addinstallationForm.customer_name,
        Address: this.addinstallationForm.Address,
        Appointment_date: this.addinstallationForm.Appointment_date,
        Created_date: this.addinstallationForm.Created_date,
        Modified_date: this.addinstallationForm.Modified_date,
        Status: this.addinstallationForm.Status,
        read, // property shorthand
      };
      this.addinstallation(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addinstallationModal.hide();
      this.initForm();
    },
    editinstallation(installation) {
      this.editForm = installation;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editinstallationModal.hide();
      let read = false;
      if (this.editForm.read[0]) read = true;
      const payload = {
        customer_name: this.addinstallationForm.customer_name,
        Address: this.addinstallationForm.Address,
        Appointment_date: this.addinstallationForm.Appointment_date,
        Created_date: this.addinstallationForm.Created_date,
        Modified_date: this.addinstallationForm.Modified_date,
        Status: this.addinstallationForm.Status,
        read,
      };
      this.updateinstallation(payload, this.editForm.id);
    },
    updateinstallation(payload, installationID) {
      const path = `http://localhost:5000/Installations/${installationID}`;
      axios.put(path, payload)
        .then(() => {
          this.getinstallations();
          this.message = 'installation updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getinstallations();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editinstallationModal.hide();
      this.initForm();
      this.getinstallations(); // why?
    },
    removeInstallation(installationID) {
      const path = `http://localhost:5000/installations/${installationID}`;
      axios.delete(path)
        .then(() => {
          this.getinstallations();
          this.message = 'installation removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getinstallations();
        });
    },
    onDeleteinstallation(installation) {
      this.removeinstallation(installation.id);
    },
  },
  created() {
    this.getinstallations();
  },
};
</script>
