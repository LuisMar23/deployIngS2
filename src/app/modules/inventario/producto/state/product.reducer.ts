import {createReducer, on} from "@ngrx/store";
import {ProductState} from "./product.state";
import {productAction} from "./product.action";

const initialState:ProductState = {
  products:[],
  product:null,
  isLoading:false,
  error:null
}
export const productReducer = createReducer(
  initialState,
  on(productAction.addProduct, (state) => {
    return{
      ...state,
      isLoading: true
    }
  }),
  on(productAction.addProductSuccess, (state, payload) => {
    return {
      ...state,
      products: [...state.products, payload.product],
      isLoading: false
    }
  }),
  on(productAction.addProductFailure, (state, payload) =>{
    return{
      ...state,
      isLoading: false,
      error: payload.error
    }
  }),
  on(productAction.loadProducts, (state) => {
    return{
      ...state,
      isLoading: true
    }
  }),
  on(productAction.loadProductsSuccess, (state, {products}) => {
    return {
      ...state,
      products: [...state.products, ...products],
      isLoading: false
    }
  }),
  on(productAction.loadProductsFailure, (state, payload) => {
    return {
      ...state,
      isLoading: false,
      error: payload.error
    }
  })
)
