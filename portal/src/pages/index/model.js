export default {
    namespace:'home',
    state:{
        author:'stonenice',
        entranceList:[{
            code:'primary_school',
            name:'小学划片'
        },{
            code:'primary_to_middle',
            name:'小升初'
        },{
            code:'school_house',
            name:'学区房'
        }],
        areaListOfCity:[{
            name:'青羊区'
        },{
            name:'天府新区'
        },{
            name:'高新区'
        },{
            name:'锦江区'
        },{
            name:'武侯区'
        },{
            name:'金牛区'
        },{
            name:'成华区'
        },{
            name:'双流区'
        },{
            name:'龙泉驿区'
        },{
            name:'郫都区'
        },{
            name:'新都区'
        },{
            name:'青北江区'
        }]
    },
    reducers:{
        changeAuthor(state,{payload}){
            return {...state,
                author:payload
            }
        }
    }

}