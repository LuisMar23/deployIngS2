import { User } from './usuario';
export interface IJWTResponse{
    access:string,
    refresh:string,
    user:User
}