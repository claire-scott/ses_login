export type IUser = {
    id: number,
    password: string,
    last_login: Date,
    is_superuser: boolean,
    username: string,
    first_name: string,
    last_name: string,
    is_staff: boolean,
    is_active: boolean,
    date_joined: Date,
    email: string,
}

export type IUnit = {
    id: number,
    name: string,
    linking_key: string,
    created_at: Date,
    created_by: IUser,
}

export type IUserUnit = {
    id: int
}