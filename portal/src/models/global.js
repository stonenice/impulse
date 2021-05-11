export default {
    namespace:'system',
    state:{
        currentActiveTab:'home'
    },
    reducers:{
        changeAppTag(state,{payload}){
            return {...state,
                currentActiveTab:payload
            }
        }
    }

}