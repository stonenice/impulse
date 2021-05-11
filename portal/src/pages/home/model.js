export default {
    namespace:'home',
    state:{
        author:'stonenice'
    },
    reducers:{
        changeAuthor(state,{payload}){
            return {...state,
                author:payload
            }
        }
    }

}