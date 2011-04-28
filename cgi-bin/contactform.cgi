#!/usr/local/bin/perl
$mail_prog = '/usr/sbin/sendmail' ;
# This script was generated automatically by Visual Form Mail: http://www.oneseek.com

&GetFormInput;

$name = $field{'name'} ;	 
$email = $field{'email'} ;	 
$address = $field{'address'} ;	 
$city = $field{'city'} ;	 
$state = $field{'state'} ;	 
$zipcode = $field{'zipcode'} ;	 
$telephone = $field{'telephone'} ;	 
$comments = $field{'comments'} ;	 

$message = "" ;
$found_err = "" ;

$errmsg = "<p>Please enter a valid email address</p>\n" ;

if (($email =~ /(@.*@)|(\.\.)|(@\.)|(\.@)|(^\.)/) || ($email !~ /^.+\@(\[?)[a-zA-Z0-9\-\.]+\.([a-zA-Z0-9]+)(\]?)$/)) {
	$message = $message.$errmsg ;
	$found_err = 1 ; }

if ($found_err) {
	&PrintError; }


$recip = "flanzz\@aol.com" ;
$frm_ = "$name , $email" ;
$sbj_ = "Allgreen contact request form" ;
$hd_ = $recip.$frm_.$sbj ;
if (($hd =~ /(\n|\r)/m) || ($recip =~ /(@.*@)|(\.\.)|(@\.)|(\.@)|(^\.)/) || ($recip !~ /^.+\@(\[?)[a-zA-Z0-9\-\.]+\.([a-zA-Z0-9]+)(\]?)$/)) {
print "Fatal Error - Invalid email" ; 
exit 0; 
}

open (MAIL, "|$mail_prog -t");
print MAIL "To: $recip\n";
print MAIL "Reply-to: $frm_\n";
print MAIL "From: $frm_\n";
print MAIL "Subject: $sbj_\n";
print MAIL "Content-type: text/html\n\n";
print MAIL "\n\n";
print MAIL "<font face=arial size=3>\n" ;
print MAIL "\n" ;
print MAIL "<b>Name:</b> ".$name."<br>\n" ;
print MAIL "<b>Email Address:</b> ".$email."<br>\n" ;
print MAIL "<b>Address:</b> ".$address."<br>\n" ;
print MAIL "<b>City:</b>".$city." <b>State:</b> ".$state." <b>Zip:</b> ".$zipcode."<br>\n" ;
print MAIL "<b>Telephone:</b> ".$telephone."<br>\n" ;
print MAIL "<b>Comments or Questions:</b> ".$comments."<br>\n" ;
print MAIL "\n\n";
close (MAIL);

$recip = "hpatton\@laughingwolf.com" ;
$frm_ = "$name, $email" ;
$sbj_ = "" ;
$hd_ = $recip.$frm_.$sbj ;
if (($hd =~ /(\n|\r)/m) || ($recip =~ /(@.*@)|(\.\.)|(@\.)|(\.@)|(^\.)/) || ($recip !~ /^.+\@(\[?)[a-zA-Z0-9\-\.]+\.([a-zA-Z0-9]+)(\]?)$/)) {
print "Fatal Error - Invalid email" ; 
exit 0; 
}

open (MAIL, "|$mail_prog -t");
print MAIL "To: $recip\n";
print MAIL "Reply-to: $frm_\n";
print MAIL "From: $frm_\n";
print MAIL "Content-type: text/html\n\n";
print MAIL "\n\n";
print MAIL "<font face=arial size=3>\n" ;
print MAIL "\n" ;
print MAIL "<b>Name:</b> ".$name."<br>\n" ;
print MAIL "<b>Email Address:</b> ".$email."<br>\n" ;
print MAIL "<b>Address:</b> ".$address."<br>\n" ;
print MAIL "<b>City:</b>".$city." <b>State:</b> ".$state." <b>Zip:</b> ".$zipcode."<br>\n" ;
print MAIL "<b>Telephone:</b> ".$telephone."<br>\n" ;
print MAIL "<b>Comments or Questions:</b> ".$comments."<br>\n" ;
print MAIL "\n\n";
close (MAIL);
print "Location: http://www.allgreenirrigation.com/index.html\nURI: http://www.allgreenirrigation.com/index.html\n\n" ;

sub PrintError { 
print "Content-type: text/html\n\n";
print $message ;
print "<p> Please use your browser's Back button to return to the form. </p>" ;

exit 0 ;
return 1 ; 
}
sub GetFormInput {

	(*fval) = @_ if @_ ;

	local ($buf);
	if ($ENV{'REQUEST_METHOD'} eq 'POST') {
		read(STDIN,$buf,$ENV{'CONTENT_LENGTH'});
	}
	else {
		$buf=$ENV{'QUERY_STRING'};
	}
	if ($buf eq "") {
			return 0 ;
		}
	else {
 		@fval=split(/&/,$buf);
		foreach $i (0 .. $#fval){
			($name,$val)=split (/=/,$fval[$i],2);
			$val=~tr/+/ /;
			$val=~ s/%(..)/pack("c",hex($1))/ge;
			$name=~tr/+/ /;
			$name=~ s/%(..)/pack("c",hex($1))/ge;

			if (!defined($field{$name})) {
				$field{$name}=$val;
			}
			else {
				$field{$name} .= ",$val";
				
				#if you want multi-selects to goto into an array change to:
				#$field{$name} .= "\0$val";
			}


		   }
		}
return 1;
}

