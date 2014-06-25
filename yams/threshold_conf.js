/* Example threshold config
 * 
 * Make sure to define all thresholds in window.thresholds
 */

window.thresholds = [
    
    //template
    /*{
	q: 'dd[data=]',
	gt: 1,
	lt: 1
    }*/

    // alert when the count of a certain process is below 1
    {
	q: 'dd[data|=count_of_]',
	lt: 1
    },

    // alert when the cpu load is above 80%
    {
	q: 'dd[data=cpu_usage]',
	gt: 60
    },

    // alert when the disk usage is above 80%
    {
	q: 'dd[data=root_disk_usage]',
	gt: 60
    }

];