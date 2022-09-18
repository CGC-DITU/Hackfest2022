<script>
    
    class customer{
        /**
         * @param {String} name
         */
        constructor(name){
            this.name=name;
            this.monthly_bill=[new monthlybill(1,12)];
            
        }
        gettotal(){
        }
        
    }
    function addbill(){
        selectedcustomer.monthly_bill=[...selectedcustomer.monthly_bill,new monthlybill((selectedcustomer.monthly_bill.length)%12 + 1,units)];
    }
    class monthlybill{
        /**
         * @param {number} units
         * @param {number} month
         */
        constructor(month,units){
            this.month=month;
            this.units=units;
            if(units<50){
                this.bill = units*2;
            }else if(units<200){
                this.bill = 100+(units-50)*2.5;
            }else if(units<400){
                this.bill = 375+(units-200)*3;
            }else if(units<500){
                this.bill = 975+(units-400)*3.5;
            }else{
                this.bill = 1325+(units-5)*4;
            }
            
        }

    }
    let customers=[new customer("Mandar"),new customer("Manas"),new customer("Manav"),new customer("Manik"),new customer("Abhigyan")];
    let selectedcustomer = customers[1];
    let units = 0;
</script>
<main class="p-4 bg-stone-200 h-screen text-xl grid place-items-center">
    <div class="bg-teal-400 grid w-4/5 rounded-3xl place-items-center shadow-2xl p-10">
    <lable class="my-2 text-3xl">Customer Name</lable>
    <select class="rounded-lg px-2 my-2 w-4/5" bind:value={selectedcustomer}>
        {#each customers as s}
            <option class="rounded-lg px-3 w-4/5" value={s}>{s.name}</option>
        {/each}
    </select>
    <div class="my-2 w-full flex justify-center">
        <lable >Units</lable>
        <input class="rounded-lg px-3 w-[70%] mx-5" type="number" bind:value={units}>
        <button class=" bg-slate-100 px-2 py-1 rounded-2xl hover:bg-blue-200" on:click={addbill}> submit</button>
    </div>
    {#if selectedcustomer}
    <div class="w-full grid place-items-center">

        <div>{selectedcustomer.name}</div>
        <table class="m-1 p-5 w-4/5 bg-white-200 shadow-2xl"  >
            <tr >
                <th class="bg-white border-2 border-black ">month</th>
                <th class="bg-white border-2 border-black">units</th>
                <th class="bg-white border-2 border-black">bill</th>
            </tr>
            {#each selectedcustomer.monthly_bill as mb}
            <tr class="px-3">
                <td class="px-3 bg-white border-2 border-black">{mb.month}</td>
                <td class="px-3 bg-white border-2 border-black">{mb.units}</td>
                <td class="px-3 bg-white border-2 border-black">{mb.bill}</td>
            </tr>
            {/each}
        </table>
    </div>
    {/if}</div>
</main>
<!-- done -->