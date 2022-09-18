<script>
    class student{
        
        /**
         * @param {any} name
         * @param {any} rollno
         */
        constructor(name,rollno){
            this.name=name;
            this.rollno=rollno;
            /**
             * @type {any[]}
             */
            this.books=[];
            this.fine=0;
        }
        
    }
    class books{
        /**
         * @param {String} bookname
         * @param {any} id
         */
        constructor(bookname,id){
            this.bookname=bookname;
            this.id=id;
            this.date = new Date();
            this.fine=0;
        }
        
    }
    let std = [new student("mandar","10000"),new student("sagar","10001"),new student("sanket","10002"),new student("saurabh","10003"),new student("siddhesh","10004"),new student("siddhant","10005"),new student("siddharth","10006"),new student("siddhesh","10007")];

    function Issuebook(){

        bt.fine = _fine;
        bt.date=(_date)
        let a =new Date().getTime() 
        let b = new Date(_date).getTime()
        let diffDays = Math.floor((a-b)/(1000*3600*24));
        
        if(diffDays<7){
            bt.fine=(diffDays)*5;
        }else if(diffDays>7){
            bt.fine=35+(diffDays-7)*20;
        }else if(diffDays>14){
            bt.fine=35+140+(diffDays-14)*50;
        }
        st.books=[...st.books,bt]
        st;
        bt='';
    }
    
    let bk = [new books("maths","1"),new books("science","2"),new books("english","3"),new books("hindi","4"),new books("computer","5")];
    

    /**
     * @type {student}
     */
    let st;
    /**
     * @type {any}
     */
    let bt;
    /**
     * @type {Date}
     */
    let _date;
    
    let _fine = 0;
    function getfine(){
        _fine = st.books.reduce((a,b)=>a+b.fine,0);
    }
</script>
<main class="text-xl bg-stone-200 h-screen grid place-items-center p-4">

 <div class="text-5xl bg-teal-300 rounded-full px-6 py-2" >Issue books </div>
<div class="grid columns-2 bg-teal-500 py-4 px-32 w-4/5 h-[50vh] rounded-3xl shadow-2xl">
    <lable class="text-3xl mt-4">student name</lable>
    <select bind:value={st} on:select={getfine}>
        {#each std as s}
        <option value={s}>{s.name}</option>
        {/each}
        </select>
    <lable class="text-3xl mt-4" >book name</lable>
    <select bind:value={bt}>
        {#each bk as b}
        <option value={b}>{b.bookname}</option>
        {/each}
        </select>
    <lable class="text-3xl mt-4">Return date</lable>
        <input bind:value={_date}  type="date"/>

        <button on:click={Issuebook} class="px-2 py-1 bg-white w-min h-min m-2 rounded-2xl hover:bg-blue-200">submit</button>
</div>
<div class="grid w-4/5 shadow-2xl">

    <lable class=" mx-20 ">student name</lable>
    <select bind:value={st}  class=" mx-20 my-2 w-64">
        {#each std as s}
        <option value={s}>{s.name}</option>
        {/each}
        </select>
        {#if st}
        <table class="m-4 p-1 max-w-full rounded-md">
            <tr class="border-2 border-black rounded-md shadow-2xl">
                <th class="p-4 border-2 border-black bg-blue-200">Name</th>
                <th class="p-4 border-2 border-black bg-blue-200">Id</th>
                <th class="p-4 border-2 border-black bg-blue-200">due date</th>
                <th class="p-4 border-2 border-black bg-blue-200">fine</th>
            </tr>
            {#each st.books as mb}
            <tr class="border-2 border-black ">
                <td class="px-4 py-2 border-2 border-black">{mb.bookname}</td>
                <td class="px-4 py-2 border-2 border-black">{mb.id}</td>
                <td class="px-4 py-2 border-2 border-black">{mb.date}</td>
                <td class="px-4 py-2 border-2 border-black">{mb.fine }</td>
            </tr>
            {/each}
        </table>
        <p class="p-5 text-bold">
            {_fine} <button on:click={getfine}>get fine</button>
        </p>
        {/if}
</div>

</main>

<!-- done -->