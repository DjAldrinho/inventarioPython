<template lang="html">
  <div class="container">
    <div class="col text-left">
      <h1>Listado de productos</h1>
      <div class="col-md-12">
        <b-table striped hover :items="productos" :fields="fields">
          <template v-slot:cell(actions)="row">
            <b-button size="sm" variant="primary" v-b-modal.modal-1 @click="sendInfo(row.item)">Editar</b-button>
            <b-button size="sm" variant="danger" @click="eliminarProducto(row.item)">Eliminar</b-button>
          </template>
        </b-table>
        <b-modal id="modal-1" title="Editar Producto" hide-footer>
          <template>
            <div>
              <b-form @submit="onSubmit">
                <b-form-group
                  id="input-group-1"
                  label="Nombre:"
                  label-for="input-1"
                >
                  <b-form-input
                    id="input-1"
                    v-model="selectedProducto.nombre"
                    type="text"
                    required
                  ></b-form-input>
                </b-form-group>
                 <b-form-group
                  id="input-group-2"
                  label="Descripcion:"
                  label-for="input-2"
                >
                  <b-form-input
                    id="input-2"
                    v-model="selectedProducto.descripcion"
                    type="text"
                    required
                  ></b-form-input>
                </b-form-group>
                <b-form-group
                  id="input-group-3"
                  label="Cantidad:"
                  label-for="input-3"
                >
                  <b-form-input
                    id="input-3"
                    v-model="selectedProducto.cantidad"
                    type="text"
                    required
                  ></b-form-input>
                </b-form-group>
                 <b-form-group
                  id="input-group-4"
                  label="Precio:"
                  label-for="input-4"
                >
                  <b-form-input
                    id="input-4"
                    v-model="selectedProducto.precio"
                    type="text"
                    required
                  ></b-form-input>
                </b-form-group>
                 <b-button type="submit" variant="primary">Submit</b-button>
                 <b-button type="reset" variant="danger">Reset</b-button>
              </b-form>
            </div>
          </template>
        </b-modal>
      </div>
    </div>
  </div>
</template>
<script>
    import axios from 'axios'

    export default {
        data() {
            return {
                fields: [
                    {key: 'nombre', label: 'Nombre'},
                    {key: 'descripcion', label: 'Descripcion'},
                    {key: 'cantidad', label: 'Cantidad'},
                    {key: 'precio', label: 'Precio'},
                    {key: 'actions', label: ''},
                ],
                productos: [],
                selectedProducto: '',
            }

        },
        methods: {
            onSubmit(evt) {
              evt.preventDefault()
              const path = 'http://localhost:8000/api/v1.0/productos/' + this.selectedProducto.id + ' /';
              axios.put(path, this.selectedProducto).then((response) => {
                    console.log(response)
                  window.location.reload();
                }).catch((error) => {
                    console.log(error)
                })
            },
            getProductos() {
                const path = 'http://localhost:8000/api/v1.0/productos/';
                axios.get(path).then((response) => {
                    this.productos = response.data
                }).catch((error) => {
                    console.log(error)
                })
            },
            sendInfo(item) {
                this.selectedProducto = item;
            },
            eliminarProducto(item){
                 const path = 'http://localhost:8000/api/v1.0/productos/' + item.id + ' /';
                axios.delete(path).then((response) => {
                    window.location.reload();
                }).catch((error) => {
                    console.log(error)
                })
            }
        },
        created() {
            this.getProductos()
        }

    }
</script>
