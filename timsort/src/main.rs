extern crate rand;
use rand::Rng;
use std::time::Instant;
const TAM: usize = 10000;

fn main() {
  let mut s: [i32;TAM] = [0; TAM];
  for _k in 0..10{
    for _i in 0..TAM {
      let random_number = rand::thread_rng().gen_range(1, 10000);
      s[_i] = random_number;
    }
  
    /*for _i in 0..TAM {
      print!("{} | ", s[_i]);
    }*/
    let start = Instant::now();
    tim_sort(&mut s, 0, TAM );
    let elapsed = start.elapsed();
    println!("tiempo: {:?}",elapsed.as_secs_f64());
    /*for _i in 0..TAM {
      print!("{} | ", s[_i]);
    }*/
  }
}

fn insertion_sort(s: &mut[i32; TAM], left: usize, right: usize) {
  for i in left..right {
    let mut j = i;
      while j > 0 && s[j] < s[j - 1] {
        s.swap(j, j - 1);
        j = j - 1;
    }
  }
}

fn merge(arr: &mut[i32; TAM], left: usize, mid: usize, right: usize) {
    let n1 = mid - left;
    let n2 = right - mid;
    let l1 = arr.clone();
    let r1 = arr.clone();
    let l = &l1[left..mid];
    let r = &r1[mid..right];
    
    let mut i = 0;
    let mut j = 0;
    let mut k = left;
    while i < n1 && j < n2 {
        if l[i] < r[j] {
            arr[k] = l[i];
            i = i + 1;
        } else {
            arr[k] = r[j];
            j = j + 1;
        }
        k = k + 1;
    }
    while i < n1 {
        arr[k] = l[i];
        i = i + 1;
        k = k + 1;
    }
    while j < n2 {
        arr[k] = r[j];
        j = j + 1;
        k = k + 1;
    }
}

fn tim_sort(arr: &mut[i32; TAM], left: usize, right: usize) {
  if (right - left) < 64 {
    insertion_sort(arr, left, right);
  }
  else {
    let mid = left + (right - left) / 2;
    tim_sort(arr, left, mid);
    tim_sort(arr, mid, right);
    merge(arr, left, mid, right);
  }
}